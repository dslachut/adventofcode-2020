from sys import argv
import numpy as np

with open("../input.txt") as FILE:
  lines = [l.strip().split(' ') for l in FILE.readlines()]

pwds = []
for l in lines:
  pwd = dict()
  pwd['min'], pwd['max'] = (int(n) for n in l[0].split('-'))
  pwd['letter'] = l[1][0]
  pwd['pwd'] = l[2]
  pwds.append(pwd)

if argv[1] == "first":
  valid = []
  for pwd in pwds:
    count = np.sum(np.array(list(pwd['pwd'])) == pwd['letter'])
    if pwd['min'] <= count <= pwd['max']:
      valid.append(True)
    else:
      valid.append(False)
  print(sum(valid))

elif argv[1] == "second":
  valid = []
  for pwd in pwds:
    idx1 = pwd['min'] - 1
    idx2 = pwd['max'] - 1
    if idx1 < len(pwd['pwd']):
      val1 = pwd['pwd'][idx1]
    else:
      val1 = ''
    if idx2 < len(pwd['pwd']):
      val2 = pwd['pwd'][idx2]
    else:
      val2 = ''
    if val1 == val2:
      valid.append(False)
    elif val1 == pwd['letter']:
      valid.append(True)
    elif val2 == pwd['letter']:
      valid.append(True)
    else:
      valid.append(False)
  print(sum(valid))
