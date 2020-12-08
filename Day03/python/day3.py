from sys import argv

import numpy as np

def scoot(field, r_stride, d_stride):
  positions = []
  pos = [0, 0]
  while pos[0] < len(field):
    positions.append(tuple(pos))
    pos[0] += d_stride
    pos[1] += r_stride
    pos[1] %= len(field[0])
  ct_trees = 0
  for r,c in positions:
    ct_trees += field[r][c]
  return ct_trees

with open("../input.txt") as FILE:
  rows = [list(np.array(list(l.strip())) == '#') for l in FILE.readlines()]

if argv[1] == "first":
  print(scoot(rows, 3, 1))
  
elif argv[1] == "second":
  A = scoot(rows, 1, 1)
  B = scoot(rows, 3, 1)
  C = scoot(rows, 5, 1)
  D = scoot(rows, 7, 1)
  E = scoot(rows, 1, 2)
  print(A, B, C, D, E, A*B*C*D*E)
