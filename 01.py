#!/usr/bin/env python3

#
# thehungryturnip@gmail.com
#
# Advent of Code 2019: Day 01
#

import sys


fuel = 0
with open(sys.argv[1], 'r') as f:
    for l in f:
        # print(int(l) // 3 - 2)
        fuel += int(l) // 3 - 2

print(f'[01a] Total fuel cost is {fuel}.')
