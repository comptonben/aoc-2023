import os
import math

from itertools import cycle

data = []
with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "input.txt"), "r") as file:
    data = file.readlines()

directions = data[0].strip()
directions = cycle(0 if d == 'L' else 1 for d in directions)
maps = {d.split('=')[0].strip(): tuple(d.split('=')[1].strip().strip('()').split(', ')) for d in data[2:]}

# part 1
step = 'AAA'
for steps, dir in enumerate(directions, start=1):
    step = maps[step][dir]
    if step == 'ZZZ':
        break

print(f"part 1: {steps}")

# part 2
step = [key for key in maps.keys() if key.endswith('A')]
counts = []
for s in step:
    for steps, dir in enumerate(directions, start=1):
        s = maps[s][dir]
        if s.endswith('Z'):
            counts.append(steps)
            break

print(f"part 2: {math.lcm(*counts)}")
