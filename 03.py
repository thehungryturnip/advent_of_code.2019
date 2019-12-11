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

def get_points(wire_def):
    points = set()
    point = 0
    for s in wire_def.split(','):
        delta = DIRECTION_DELTAS[s[0]]
        length = int(s[1:])
        for i in range(length):
            point += delta
            points.add(point)
    return points

def distance_to_origin(point):
    return int(abs(point.real) + abs(point.imag))

with open(sys.argv[1], 'r') as f:
    wires = [l.strip() for l in f]
pairs = [wires[i:i+2] for i in range(0, len(wires), 2)]

for p in pairs:
    print('\n'.join(p))
    points_0 = get_points(p[0])
    points_1 = get_points(p[1])
    intersections = points_0.intersection(points_1)
    closest = 0
    for i in intersections:
        distance = distance_to_origin(i)
        if closest == 0 or distance < min_distance:
            closest = i
            min_distance =  distance
    print(f'[03a] The intersection closest to the origin is at {closest} with'
          f' a distance of {min_distance}.')
