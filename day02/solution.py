import os
import re
import operator
import functools

# part 1
game_reqs = {'red': 12, 'green': 13, 'blue': 14}
data = []
sum = 0
with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "input.txt"), "r") as file:
    data = file.readlines()

for d in data:
    imp = False
    s_d = re.split(r'[:,;]', d)
    for s in s_d[1:]:
        if int(s.split()[0]) > game_reqs[s.split()[1]]:
            imp = True
    if imp:
        continue

    sum += int(s_d[0].split()[1])

print(f"part 1: {sum}")



# part 2
data = []
sum = 0
with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "input.txt"), "r") as file:
    data = file.readlines()

for d in data:
    game_reqs = {'red': 0, 'green': 0, 'blue': 0}
    s_d = re.split(r'[:,;]', d)
    for s in s_d[1:]:
        game_reqs[s.split()[1]] = max(int(s.split()[0]), game_reqs[s.split()[1]])

    sum += functools.reduce(operator.mul, game_reqs.values(), 1)

print(f"part 2: {sum}")
