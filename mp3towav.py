# -*- coding: utf-8 -*-
"""
@author: Ankit

This script converts mp3 audio files to corresponding wav files

"""

import os
from os import path
from pydub import AudioSegment

AudioSegment.converter = "C:\\ffmpeg\\bin\\ffmpeg.exe"
AudioSegment.ffmpeg = "C:\\ffmpeg\\bin\\ffmpeg.exe"
AudioSegment.ffprobe ="C:\\ffmpeg\\bin\\ffprobe.exe"

src = "C:\\Users\\Ankit\\Desktop\\Scalable_Audio_Captcha\\audio_captcha_training_set\\"
dest = "C:\\Users\\Ankit\\Desktop\\Scalable_Audio_Captcha\\audio_captcha_wav\\"

for file in os.listdir(src):
    if(file.endswith('mp3')):
        full_path = (os.path.join(src, file))
        sound = AudioSegment.from_mp3(full_path)
        sound.export( dest + file.split('.')[0] + '.wav', format = 'wav' )
