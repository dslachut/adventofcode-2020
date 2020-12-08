from sys import argv, exit

with open("../input.txt") as FILE:
  raw_data = FILE.read()

"""
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
"""
fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]

entries = []
for entry in [e.strip().split() for e in raw_data.split("\n\n")]:
  entries.append(dict([f.split(':') for f in entry]))

# initial validation
valid = []
invalid = []
for entry in entries:
  for f in fields[:-1]:
    if f not in entry.keys():
      invalid.append(entry)
      break
  else:
    valid.append(entry)

if argv[1] == "first":
  print("Valid:  ", len(valid))
  print("Invalid:", len(invalid))
  exit(0)

if argv[1] != "second":
  exit(0)

"""
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
  If cm, the number must be at least 150 and at most 193.
  If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
"""

eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

validated = []

for entry in valid:
  if (len(entry["byr"]) != 4) or (int(entry["byr"]) < 1920) or (int(entry["byr"]) > 2002):
    invalid.append(entry)
  elif (len(entry["iyr"]) != 4) or (int(entry["iyr"]) < 2010) or (int(entry["iyr"]) > 2020):
    invalid.append(entry)
  elif (len(entry["eyr"]) != 4) or (int(entry["eyr"]) < 2020) or (int(entry["eyr"]) > 2030):
    invalid.append(entry)
  elif entry["hgt"][-2:].lower() not in ['cm', 'in']:
    invalid.append(entry)
  elif (entry["hgt"][-2:].lower() == 'cm') and ((int(entry["hgt"][:-2]) < 150) or (int(entry["hgt"][:-2]) > 193)):
    invalid.append(entry)
  elif (entry["hgt"][-2:].lower() == 'in') and ((int(entry["hgt"][:-2]) < 59) or (int(entry["hgt"][:-2]) > 76)):
    invalid.append(entry)
  elif (len(entry["hcl"]) != 7) or (entry["hcl"][0] != "#"):
    invalid.append(entry)
  elif entry["ecl"] not in eye_colors:
    invalid.append(entry)
  elif len(entry["pid"]) != 9:
    invalid.append(entry)
  else:
    try:
      _ = int(entry["hcl"][1:], base=16)
      _ = int(entry["pid"])
      validated.append(entry)
    except ValueError:
      invalid.append(entry)

print("Valid:    ", len(valid))
print("Validated:", len(validated))
print("Invalid:  ", len(invalid))
