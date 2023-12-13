import os

data = []
with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "input.txt"), "r") as file:
    data = file.readlines()

# part 1
res = 0
history = []
for d in data:
    history = []
    history.append([int(_d) for _d in d.strip().split()])
    while not all(x == 0 for x in history[-1]):
        history.append([history[-1][i] - history[-1][i - 1] for i in range(1, len(history[-1]))])
    tmp = 0
    for i in range(len(history)-1, -1, -1):
        tmp += history[i][-1]
    res += tmp

print(f"part 1: {res}")

# part 2
res = 0
history = []
for d in data:
    history = []
    history.append([int(_d) for _d in d.strip().split()])
    while not all(x == 0 for x in history[-1]):
        history.append([history[-1][i] - history[-1][i - 1] for i in range(1, len(history[-1]))])
    tmp = 0
    for i in range(len(history)-1, 0, -1):
        tmp = history[i-1][0] - tmp
    res += tmp

print(f"part 2: {res}")
