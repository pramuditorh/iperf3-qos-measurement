#!/bin/bash

while getopts p:i:f:l:h: flag
do
  case "${flag}" in
    p) port=${OPTARG};;
    i) interval=${OPTARG};;
    f) filename=${OPTARG};;
    l) loops=${OPTARG};;
    h) echo "Script to take QoS measurement using Iperf3"
       echo "How to USE: ./server.sh -p [PORT] -i [INTERVAL] -f [FILENAME] -l [LOOPS]";;
  esac
done

echo "port: $port"
echo "interval: $interval"
echo "filename: $filename"
echo "loops: $loops"

for (( c=1; c<=$loops; c++ ))
do
  echo "DO $filename-$c"
  iperf3 --server --port $port --interval $interval -1 > $filename-$c.txt
  echo "DONE $filename-$c"
  sleep 3
done