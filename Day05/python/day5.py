import sys

with open('../input.txt') as FILE:
    tickets = [
        l.strip()\
        .replace('F', '0')\
        .replace('B', '1')\
        .replace('R', '1')\
        .replace('L', '0') 
        for l in FILE.readlines()
    ]
    tickets = [
        [int(t[:-3], base=2), int(t[-3:], base=2)]
        for t in tickets
    ]
    tickets = [
        [t[0], t[1], t[0] * 8 + t[1]]
        for t in tickets
    ]

stix = sorted(tickets, key=lambda x:x[2])

if sys.argv[1].lower() == "first":
    print(stix[-1][-1])
    sys.exit(0)
if sys.argv[1].lower() != "second":
    sys.exit(1)

ids = list(zip(*stix))[2]

print(max(set(range(stix[-1][-1] + 1)).difference(ids)))
