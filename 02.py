#!/usr/bin/env python3

#
# thehungryturnip@gmail.com
#
# Advent of Code 2019: Day 02
#

import sys

ops = {
        1: lambda x, y : x + y,
        2: lambda x, y : x * y,
        }

def run(prog):
    prog = prog[:]
    p = 0
    while not prog[p] == 99:
        opcode = prog[p]
        arg_1 = prog[prog[p + 1]]
        arg_2 = prog[prog[p + 2]]
        prog[prog[p + 3]] = ops[opcode](arg_1, arg_2)
        p = p + 4
    return prog[0]

if sys.argv[1] == '02.in':
    testing = False
else:
    testing = True

progs = []
with open(sys.argv[1], 'r') as f:
    for l in f.read().splitlines():
        if l:
            prog = l.split(',')
            prog = [int(n) for n in prog]
            progs.append(prog)

if testing:
    for p in progs:
        print(p)
        out = run(p)
        print(out)

if not testing:
    VALUE_1 = 12
    VALUE_2 = 2
    TARGET = 19690720
    p = progs[0][:]
    p[1] = VALUE_1
    p[2] = VALUE_2
    print(f'[02a] The value at position 0 is {run(p)}.')

    for noun in range(100):
        for verb in range(100):
            p = progs[0][:]
            p[1] = noun
            p[2] = verb
            if run(p) == TARGET:
                print(f'[02b] 100 * {noun} + {verb} = {100 * noun + verb} yields {TARGET}.')
