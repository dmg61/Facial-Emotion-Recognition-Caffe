#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

root = "/home/bliq/Work/Facial_Emotion_Recognition/Test/"

print "Begin remove files"

for i in range(1, 9):
    for path, subdirs, files in os.walk(root + str(i)):
        for name in [f for f in files if f.endswith(".csv")]:
            os.remove(root + str(i) + "/" + name)

print "Cancle remove files"
