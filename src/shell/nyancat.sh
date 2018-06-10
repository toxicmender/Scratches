#!/usr/bin/env bash

# Required packages:
# sudo apt install nyancat mpv
# the video file should obviously be present at the specified location
NYAA='/home/danish/Videos/youtube/Nyan_Cat_original.mp4'
mpv --loop-file=inf --no-video $NYAA &
nyancat
