#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

inFile = open("emotion_test.txt", 'w')

root = "/home/bliq/Work/Facial_Emotion_Recognition/Test/"

filenames = []
# path = os.path.join(root, "targetdirectory")

print "Begin read filename"

for i in range(1, 9):
    for path, subdirs, files in os.walk(root + str(i)):
        for name in [f for f in files if f.endswith(".png")]:
            inFile.write(os.path.join(path, name) + " " + str(i) + "\n")

inFile.close()
