#!/usr/bin/env bash
ffmpeg -i demo.ogv \
       -c:v libx264 -preset veryslow -crf 22 \
       -c:a aac -b:a 160k -strict -2 \
       demo.mp4