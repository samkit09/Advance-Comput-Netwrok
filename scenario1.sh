#!/bin/bash
rm -rf ./files/input_*.txt
rm -rf ./files/output_*.txt
rm -rf ./files/*_received.txt
python3.6 Controller.py 60 &
python3.6 Node.py 0 60 1 "message from 0 to 1" &
python3.6 Node.py 1 60 -1 &
python3.6 Node.py 2 60 -1 &
python3.6 Node.py 3 60 -1 &
python3.6 Node.py 4 60 -1 &
