#!/bin/bash

while getopts s:c:p:b:t:i:l: flag
do
  case "${flag}" in
    s) server=${OPTARG};;
    c) protocol=${OPTARG};;
    p) port=${OPTARG};;
    b) bandwidth=${OPTARG};;
    t) time=${OPTARG};;
    i) interval=${OPTARG};;
    l) loops=${OPTARG};;
  esac
done

echo "server ip: ${server}"
echo "protocol: ${protocol}"
echo "port: ${port}"
echo "bandwidth: ${bandwidth}"
echo "interval: ${interval}"
echo "loops: ${loops}"

for (( c=1 ; c<=$loops; c++ ))
do
  if [ -z $protocol ]
  then
    echo "DO tcprequest-$c"
    iperf3 --client $server --port $port --bandwidth $bandwidth --time $time --interval $interval
    echo "DONE tcprequest-$c"
    sleep 5
  else
    echo "DO udprequest-$c"
    iperf3 --client $server --$protocol --port $port --bandwidth $bandwidth --time $time --interval $interval
    echo "DONE udprequest-$c"
    sleep 5
  fi
done