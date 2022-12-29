import os
import subprocess


class AdaptiveStreamer:
    def __init__(self, input_file, num_streams, video_codec, audio_codec, preset, init_crf, init_factor):
        self.input_file = input_file
        self.video_codec = video_codec
        self.audio_codec = audio_codec
        self.preset = preset
        self.crf = init_crf
        self.factor = init_factor
        self.curr_num = 0
        self.num_streams = num_streams
        self.filenames = []

    def create_stream(self):
        crf = str(self.crf)
        cwd = os.path.abspath(os.path.dirname(__file__))
        output_file = f"video_{self.curr_num}.mp4"
        subprocess.run(
            ["ffmpeg", "-i", self.input_file, "-c:v", self.video_codec, '-vf',
             f"scale=iw/{self.factor}:ih/{self.factor}",
             "-preset", self.preset, "-crf", crf, "-c:a", self.audio_codec, output_file], shell=True, cwd=cwd)
        self.filenames.append(output_file)

    def create_all_streams(self):
        while self.curr_num < self.num_streams:
            self.create_stream()
            self.crf -= 2
            self.factor += 0.5
            self.curr_num += 1

    def get_filenames(self):
        return self.filenames
