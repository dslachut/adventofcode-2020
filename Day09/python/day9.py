"""AoC 2020 Day 09"""

import sys

if sys.argv[1].lower() not in ["first", "second"]:
    sys.exit(-1)

with open('../input.txt') as FILE:
    numbers = [int(ln.strip()) for ln in FILE.readlines()]

inval = None

for i in range(25, len(numbers)):
    number = numbers[i]
    min_idx = i - 25
    max_idx = i - 1
    for j in range(min_idx, i):
        for k in range(j+1, i):
            if numbers[j] + numbers[k] == number:
                break
        else:
            continue
        break
    else:
        if sys.argv[1].lower() == "first":
            print(number)
            sys.exit(0)
        else:
            inval = (i, number)
            break

starts = list(range(len(numbers)))
next_starts = []
for region in range(2, len(numbers)):
    while len(starts) > 0:
        base = starts.pop(0)
        ns = numbers[base:base+region]
        reg_sum = sum(ns)
        if reg_sum > inval[1]:
            continue
        if reg_sum == inval[1]:
            print(min(ns) + max(ns))
            break
        next_starts.append(base)
    else:
        starts = next_starts
        next_starts = []
        continue
    break
