#!/bin/bash
rm -rf ./files/input_*.txt
rm -rf ./files/output_*.txt
rm -rf ./files/*_received.txt
python3 Controller.py 100 &
python3 Node.py 0 100 2 "message from 0 to 3" &
python3 Node.py 1 100 -1 &
python3 Node.py 2 100 -1 &
python3 Node.py 3 100 -1 &
python3 Node.py 4 100 -1 &
