#!/usr/bin/env python3

#
# thehungryturnip@gmail.com
#
# Advent of Code 2019 Day 04
#

MIN = 137683
MAX = 596253

def decreases(p):
    for i in range(len(p) - 1):
        if p[i] > p[i + 1]:
            return True
    return False

def repeats(p):
    for i in range(1, len(p)):
        if p[i - 1] == p[i]:
            return True
    return False

def distribution(p):
    dist = {}
    for i in p:
        if not i in dist:
            dist[i] = 1
        else:
            dist[i] += 1
    return dist

foo = 0
valid_1 = 0
valid_2 = 0
for p in range(MIN, MAX + 1):
    p = [int(i) for i in list(str(p))]
    if not decreases(p):
        if repeats(p):
            valid_1 += 1
        dist = distribution(p)
        if 2 in dist.values():
            valid_2 += 1
print(f'[04a] There are {valid_1} valid passwords.')
print(f'[04b] There are {valid_2} valid passwords.')
