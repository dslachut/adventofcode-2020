import sys
import numpy as np

PART = sys.argv[1].lower()
if PART not in ["first", "second"]:
    sys.exit(-1)

def first_differences(ns):
    diffs = []
    for i,n in enumerate(ns[1:]):
        diffs.append(n-ns[i])
    return diffs

def check_valid(diffs):
    for v in set(diffs):
        if v > 3:
            return False
    return True

def n_paths(source, target, graph, memo):
    total = 0
    for node in graph[source]:
        if node in memo:
            total += memo[node]
        elif node == target:
            total += 1
        else:
            total += n_paths(node, target, graph, memo)
    memo[source] = total
    return total
    

with open("../input.txt") as FILE:
    ads = sorted([int(l.strip()) for l in FILE.readlines()])

ads = [0] + ads + [ads[-1] + 3]

if PART == "first":
    diffs = np.array(first_differences(ads))
    ones = diffs == 1
    threes = diffs == 3
    print(sum(ones) * sum(threes))
    sys.exit(0)

graph = dict()
n_paths_from = dict()
for i, v in enumerate(ads):
    adj_list = [idx+i+1 for idx, val in enumerate(ads[i+1:i+4]) if val-v <= 3]
    graph[i] = adj_list
print(n_paths(0, len(ads)-1, graph, dict()))
