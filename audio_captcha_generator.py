# -*- coding: utf-8 -*-
"""

@author: Ankit

This script generates unique audio captchas consisting 8 characters using Google Text-to-Speech (ggts) service

"""

from gtts import gTTS 
import os
import random

with open('symbols.txt', 'r') as file:
    symbols = file.read().replace('\n', '')

def getunique():
    for r, d, f in os.walk(path):
        for file in f:
            if file.endswith('.mp3'):
                unique.add(file.split('.')[0])
            
            
def generate(unique):
    chars = symbols
    while True:
        value = "".join(random.choice(chars) for _ in range(8))
        if value not in unique:
            language = 'en'
            myobj = gTTS(text=value, lang=language, slow=False) 
            myobj.save("audio_captcha_training_set/"+value+".mp3")
            unique.add(value)
            break

path = "C:\\Users\\Ankit\\Desktop\\Scalable_Audio_Captcha\\audio_captcha_training_set\\"
unique = set()
getunique()

for _ in range(150000):
    generate(unique)