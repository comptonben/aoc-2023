import os

from functools import lru_cache

data = []
with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "input.txt"), "r") as file:
    data = file.read().split('\n')

# up(-1, 0), down(1, 0), left(0, -1), right(0, 1)
directions = {'north': [[-1, 0], '|', '7', 'F'], 'south': [[1, 0], '|', 'L', 'J'], 'east': [[0, 1], '-', 'J', '7'], 'west': [[0, -1], '-', 'L', 'F']}
pipes = {
    '|': ['north', 'south'],
    '-': ['east', 'west'],
    'L': ['north', 'east'],
    'J': ['north', 'west'],
    '7': ['south', 'west'],
    'F': ['south', 'east'],
    'S': ['north', 'south', 'east', 'west']
}


def get_valid_neighbors(X: list[int, int]) -> list[list[int, int]]:
    neighbor_options = []
    pipe = data[X[0]][X[1]]
    for _, op in directions.items():
        if 0 <= X[0] + op[0][0] < rows and 0 <= X[1] + op[0][1] < columns:
            neighbor_options.append([x + y for x, y in zip(X, op[0])])
        else:
            neighbor_options.append([])

    valid_neighbors = []
    neighbors = [data[n[0]][n[1]] if n else [] for n in neighbor_options]
    for i, n in enumerate(neighbors):
        if n and n != '.':
            if n in directions[list(directions.keys())[i]] and list(directions.keys())[i] in pipes[pipe]:
                valid_neighbors.append(neighbor_options[i])

    return valid_neighbors


S = []
for i, d in enumerate(data):
    if 'S' in d:
        S = [i, d.index('S')]

rows = len(data)
columns = len(data[0])

steps = [S]
size = 0
while len(steps) != size:
    size = len(steps)
    v_n = get_valid_neighbors(list(steps)[-1])
    for n in v_n:
        if n not in steps:
            steps.append(n)
            break
    if list(steps)[0] == list(steps)[-1]:
        break

# part 1
res = len(steps) // 2
print(f"part 1: {res}")

# part 2
res = 0
crossing = ['|', 'F', '7', 'S']


@lru_cache(maxsize=None)
def get_crossing(r, c):
    if [r, c] in steps and data[r][c] in crossing:
        return 1
    return 0


def get_crossings(r, c):
    crossings = 0
    for l in range(c):
        crossings += get_crossing(r, l)
    return crossings


for r in range(rows):
    for c in range(columns):
        if not [r, c] in steps:
            crossings = get_crossings(r, c)
            if (crossings % 2) == 1:
                res += 1

print(f"part 2: {res}")
print(get_crossing.cache_info())
