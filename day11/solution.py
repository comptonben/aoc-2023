import os

data = []
with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "input.txt"), "r") as file:
    data = file.read().split('\n')


def total_distance(universe: set((int, int))):
    distance = []
    c_uni = universe.copy()
    for l in universe:
        for ll in c_uni:
            if l != ll:
                distance.append(abs(l[0] - ll[0]) + abs(l[1] - ll[1]))
        c_uni.remove(l)
    return sum(distance)


# part 1
def expanded_distance(rate):
    exp = []
    for r in data:
        if '#' not in r:
            [exp.append(r) for i in range(rate-1)]
        exp.append(r)

    transposed = [''.join(r) for r in zip(*exp)]
    exp = []
    for r in transposed:
        if '#' not in r:
            [exp.append(r) for i in range(rate-1)]
        exp.append(r)

    expanded = [''.join(r) for r in zip(*exp)]
    locations = set()
    for r, row in enumerate(expanded):
        if '#' not in row:
            continue
        for c, char in enumerate(row):
            if char == '#':
                locations.add((r, c))
    return total_distance(locations)


time_points = [1, 2, 10, 100]
values = []
[values.append(expanded_distance(r)) for r in time_points]
[print(f"part 1: {r} --> {v}") for r, v in zip(time_points, values)]


# part 2
locations = set()
for r, row in enumerate(data):
    if '#' not in row:
        continue
    for c, char in enumerate(row):
        if char == '#':
            locations.add((r, c))

e_rows = [i if '#' not in row else None for i, row in enumerate(data)]
e_cols = [i if '#' not in row else None for i, row in enumerate([''.join(r) for r in zip(*data)])]

c_loc = locations.copy()
distance = []
for l in locations:
    for ll in c_loc:
        if l != ll:
            res = abs(l[0] - ll[0]) + abs(l[1] - ll[1])
            for i in range(l[0], ll[0], 1 if l[0] < ll[0] else -1):
                if e_rows[i]:
                    res += 1e6 - 1
            for i in range(l[1], ll[1], 1 if l[1] < ll[1] else -1):
                if e_cols[i]:
                    res += 1e6 - 1
            distance.append(res)
    c_loc.remove(l)

print(f"part 2: {sum(distance)}")
