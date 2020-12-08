"""AoC2020 Day 7"""

import sys

with open("../input.txt") as FILE:
    rules = [l.strip()[:-1].split(' bags contain ') for l in FILE.readlines()]

if sys.argv[1].lower() == 'first':
    to_search = ["shiny gold"]
    bags = set()
    while len(to_search) > 0:
        child = to_search.pop()
        for r in rules:
            if child in r[1]:
                if r[0] in bags:
                    continue
                bags.add(r[0])
                to_search.append(r[0])
    print(bags)
    print(len(bags))
    sys.exit(0)

if sys.argv[1].lower() != 'second':
    sys.exit(1)

new_rules = dict()
for r in rules:
    new_rules[r[0]] = []
    if r[1] == 'no other bags':
        continue
    children = [c.split() for c in r[1].split(', ')]
    for child in children:
        new_rules[r[0]].append((int(child[0]), ' '.join(child[1:3])))
rules = new_rules

to_append = ["shiny gold"]
count = 0
while len(to_append) > 0:
    parent = to_append.pop()
    children = rules[parent]
    for child in children:
        num, color = child
        count += num
        _ = [to_append.append(color) for _ in range(num)]
print(count)
