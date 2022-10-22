#!/user/bin/env python
# coding=utf-8
from ffmpy3 import FFmpeg

import os


# MP3转wav
def audio_transfor(audio_path: str, output_dir: str):
    ext = os.path.basename(audio_path).strip().split('.')[-1]
    # if ext != 'mp3' or 'flac':
    #     raise Exception('format is not mp3')

    result = os.path.join(output_dir, '{}.{}'.format(os.path.basename(audio_path).strip().split('.')[0], 'wav'))
    filter_cmd = '-f wav -ac 1 -ar 16000'
    ff = FFmpeg(inputs={audio_path: None}, outputs={result: filter_cmd})
    print(ff.cmd)
    ff.run()
    return result


def handle(audio_dir: str, output_dir: str):
    for x in os.listdir(audio_dir):
        audio_transfor(os.path.join(audio_dir, x), output_dir)