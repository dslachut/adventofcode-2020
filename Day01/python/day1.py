from sys import argv

with open("../input.txt") as FILE:
  numbers = [int(l.strip()) for l in FILE.readlines()]

if argv[1] == "second":
  for i, n1 in enumerate(numbers):
    for j, n2 in enumerate(numbers[i:]):
      for k, n3 in enumerate(numbers[i+j:]):
        if n1+n2+n3 == 2020:
          print(n1*n2*n3)
elif argv[1] == "first":
  for i, n1 in enumerate(numbers):
    for j, n2 in enumerate(numbers[i:]):
      if n1+n2 == 2020:
        print(n1*n2)
        
