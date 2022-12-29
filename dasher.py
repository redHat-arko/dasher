import os
import subprocess
import sys

import adaptive_streamer


class DASHMaker:
    def __init__(self, input_file, num_streams):
        self.input_file = input_file
        self.num_streams = num_streams
        self.filenames = []
        self.frag_filenames = []
        self.cwd = os.path.abspath(os.path.dirname(__file__))

    def create_unfragmented_files(self):
        video_codec = "libx264"
        audio_codec = "copy"
        preset = "medium"
        init_crf = 18
        init_factor = 1
        streamer = adaptive_streamer.AdaptiveStreamer(self.input_file, self.num_streams, video_codec,
                                                      audio_codec, preset, init_crf, init_factor)
        streamer.create_all_streams()
        self.filenames = streamer.get_filenames()

    def create_fragmented_files(self):
        for file in self.filenames:
            out_file = file[:-4] + "f" + ".mp4"
            subprocess.run(["mp4fragment", file, out_file], shell=True, cwd=self.cwd)
            self.frag_filenames.append(out_file)

    def create_dash_stream(self):
        self.create_unfragmented_files()
        self.create_fragmented_files()
        subprocess.run(["mp4dash"] + self.frag_filenames, shell=True, cwd=self.cwd)

    def clean_up(self):
        os.chdir(self.cwd)
        for file in self.filenames:
            os.remove(file)
        for file in self.frag_filenames:
            os.remove(file)

    def run(self):
        self.create_dash_stream()
        self.clean_up()


def main():
    input_file = sys.argv[1]
    num_streams = sys.argv[2]
    dash_maker = DASHMaker(input_file, num_streams)
    dash_maker.run()


main()
