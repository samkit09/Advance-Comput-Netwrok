#!/bin/bash
rm -rf ./files/input_*.txt
rm -rf ./files/output_*.txt
rm -rf ./files/*_received.txt
python3.6 Controller.py 160 &
python3.6 Node.py 0 160 3 "message from 2 to 4" &
python3.6 Node.py 1 160 -1 &
python3.6 Node.py 2 160 -1 &
python3.6 Node.py 3 160 -1 &
python3.6 Node.py 4 160 -1 &
