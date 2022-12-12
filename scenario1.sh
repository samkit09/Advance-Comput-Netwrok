#!/bin/bash
rm -rf input_*.txt
rm -rf output_*.txt
# python3 Controller.py 100 &
python3.6 Node.py 0 10 -1
