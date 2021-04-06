#!/home/pedro/Dev/TTSer/venv/bin/python
# -*- coding: utf-8 -*-
import os, sys, re
from subprocess import call
from gtts import gTTS
from playsound import playsound

# Read each line in book with a for loop and generate an audio file, play the audio and print the line

book_file = "beyond_good_and_evil.txt"

file1 = open(book_file, "r")

while(True):
    os.system('cls' if os.name == 'nt' else 'clear')
    line = file1.readline()
    line_to_read = line.strip()
    print(line_to_read)

    if not bool(re.match('^\s+$', line)):
        tts = gTTS(line_to_read, lang='en')
        tts.save('reading_file.wav')
        playsound('reading_file.wav')
    else:
        continue
        



file1.close












