#!/usr/env/bin python3
import sys

lines = open(sys.argv[1]).readlines()
N = int(lines.pop(0).strip())

gem = 0
keep = {}

for l in range(N):
  line = lines.pop(0)
  memo = {}
  for ch in line.strip():
    #count each character in each line one time
    if ch not in memo:
      memo[ch] = 1
      if ch in keep:
        keep[ch] += 1
      else:
        keep[ch] = 1

for key, value in keep.items():
  if value == N:
    gem += 1

print(gem)
