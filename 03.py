#!/usr/bin/env python3

#
# thehungryturnip@gmail.com
#
# Advent of Code 2019 Day 03
#

import sys

DIRECTION_DELTAS = {
    'R': 1,
    'L': -1,
    'D': 1j,
    'U': -1j,
    }

def get_units(wire):
    units = {}
    coord = 0
    steps = 0
    for s in wire.split(','):
        delta = DIRECTION_DELTAS[s[0]]
        length = int(s[1:])
        for i in range(length):
            coord += delta
            steps += 1
            units[coord] = steps
    return units

def distance_to_origin(coord):
    return int(abs(coord.real) + abs(coord.imag))

with open(sys.argv[1], 'r') as f:
    wires = [l.strip() for l in f]
pairs = [wires[i:i+2] for i in range(0, len(wires), 2)]

for p in pairs:
    print('\n'.join(p))
    units_0 = get_units(p[0])
    units_1 = get_units(p[1])
    intersections = set(units_0.keys()).intersection(set(units_1.keys()))
    closest = 0
    fastest = 0
    for c in intersections:
        distance = distance_to_origin(c)
        if closest == 0 or distance < min_distance:
            closest = c
            min_distance =  distance
        steps = units_0[c] + units_1[c]
        if fastest == 0 or steps < min_steps:
            fastest = c
            min_steps = steps
    print(f'[03a] The intersection closest to the origin is at {closest} with'
          f' a distance of {min_distance}.')
    print(f'[03b] The intersection fastest from the origin is at {fastest}'
          f' with {min_steps} steps.')
