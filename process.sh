#!/bin/bash

echo 'Running script....'

for ((c=1; c<=30; c++))
do
  echo "Print pengujian-$c.txt"
  cat pengujian-$c.txt | grep sec | head -30 | tr - " " | awk '{print $8,$10,$12$13}' > pengujian-$c-processed.txt
done
