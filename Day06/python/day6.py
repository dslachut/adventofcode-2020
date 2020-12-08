import sys

if sys.argv[1].lower() == "first":
    with open("../input.txt") as FILE:
        print(sum([len(set("".join(g.strip().split()))) for g in FILE.read().split('\n\n')]))
    sys.exit(0)

if sys.argv[1].lower() != "second":
    sys.exit(1)

with open("../input.txt") as FILE:
    groups = [g.strip().split() for g in FILE.read().split('\n\n')]
intersections = []
for g in groups:
    inter = set(g[0])
    for p in g[1:]:
        inter = inter.intersection(p)
    intersections.append(len(inter))
print(sum(intersections))
