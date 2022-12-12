#!/bin/bash
rm -rf ./files/input_*.txt
rm -rf ./files/output_*.txt
rm -rf ./files/*_received.txt
python3.6 Controller.py 16 &
python3.6 Node.py 0 16 1 "Jai Shree Ram" &
python3.6 Node.py 1 16 -1 &
