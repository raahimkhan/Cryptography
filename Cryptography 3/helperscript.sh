#!/bin/bash
x=1
while [ $x -le 1000 ]
do
  openssl aes-128-cbc -in message.txt -out message.enc -pass pass:raahim12
  x=$(( $x + 1 ))
done
