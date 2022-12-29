# dasher
Easily create an MPEG-DASH presentation of a video.

## Why use dasher
`ffmpeg` and the `Bento4` SDK, in themselves, are very powerful tools and in combination, can be used to create high-quality, highly viable streaming media.
However, they are quite daunting to use for the not-so-well-versed. `dasher` is a tool intended to make it easy to create streaming media.

## Features
* Easy conversion of unfragmented video to an MPEG-DASH compatible format.
* Adaptive streaming implemented by automatically transcoding video to different resolutions to obtain a number of user-specified streams.
* Efficient encoding using `ffmpeg`'s open-source `H.264` (`x264`) encoder.
* Encoder settings optimized for `1080p` input to deliver quality similar to `Amazon`'s `VBR` `H.264` streams, encoded using successively decreasing `CRF` values to maintain
a perceptible level of quality across resolutions.

## Dependencies
* Requires `Python` 3.7+ to be installed
* [ffmpeg](https://ffmpeg.org)
* [Bento4](https://www.bento4.com)

The source files need to be placed in the same directory as the `Bento4` and `ffmpeg` binaries.

## Usage

Place the files `adaptive_streamer.py` and `dasher.py` in the same directory as the `Bento4` and `ffmpeg` binaries and run the script using:

`python3 dasher.py <input file> <number_of_streams>`

For example:

`python3 dasher.py input.mp4 5`

will take `input.mp4` as input and create an `MPEG-DASH` manifest with 5 streams of successively decreasing resolution.
