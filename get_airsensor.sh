#!/bin/sh
cd /root/vocsensor
echo $(date +"%Y-%m-%d %H:%M:%S"),$(./airsensor -v -o) >> airsensordata.txt
gnuplot plotImage.gnuplot
convert -gravity south -fill black -annotate 0 "$(date +"%Y-%m-%d %H:%M:%S")" airsensorimage.png -compress none airsensorimage.bmp
#convert airsensorimage.png -compress none airsensorimage.bmp
./display_airsensor.py
