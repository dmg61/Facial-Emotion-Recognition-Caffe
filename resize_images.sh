#!/bin/bash

echo "##########################################"

for name in /home/bliq/Work/Facial_Emotion_Recognition/Emotion/8/*.png; do
    convert -resize 256x256\! $name $name
done

echo "Resize complite"
