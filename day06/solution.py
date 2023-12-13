import os
import math

data = []
res = 1

# part 1
with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "input.txt"), "r") as file:
    data = file.readlines()

data = [d.split(":")[1].strip().split() for d in data]
race_tuples = list(zip(data[0], data[1]))

for time, distance in race_tuples:
    time, distance = int(time), int(distance)
    options = 0
    for i in range(1, time):
        if i * (time-i) > distance:
            options += 1

    res *= options

print(f"part 1: {res}")

# part 2

race = (''.join(data[0]), ''.join(data[1]))
time, distance = int(race[0]), int(race[1])

res = 0
for i in range(1, time):
    if i * (time-i) > distance:
        res += 1

print(f"part 2: {res}")
