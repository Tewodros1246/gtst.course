#!/bin/bash

target=$1
script=$2

echo "nmap running"
nmap -sV --script=$script $target
