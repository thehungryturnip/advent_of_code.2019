#!/usr/bin/env python3

#
# thehungryturnip@gmail.com
#
# Advent of Code 2019: Day 01
#

import sys

def formula_a(weight):
    return weight // 3 - 2

def formula_b(weight):
    total = 0
    fuel = formula_a(weight)
    while fuel > 0:
        total += fuel
        fuel = formula_a(fuel)
    print(f'{weight}:{total}')
    return total

fuel_a = 0
fuel_b = 0
with open(sys.argv[1], 'r') as f:
    for l in f:
        fuel_a += formula_a(int(l))
        # print(fuel_a)
        fuel_b += formula_b(int(l))
        # print(fuel_b)

print(f'[01a] Total fuel cost is {fuel_a}.')
print(f'[01b] Total fuel cost is {fuel_b}.')
