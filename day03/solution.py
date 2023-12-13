import os

symbols_set = set()

# part 1
data = []
part_set = set()
res = 0
with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "input.txt"), "r") as file:
    data = [line.strip() for line in file.readlines()]

for d in data:
    for c in d:
        if not c.isdigit() and c != '.':
            symbols_set.add(c)

engine_map = []
for i, d in enumerate(data):
    engine_map.append([c for c in d])

for i in range(len(engine_map)):
    for j in range(len(engine_map[i])):
        if engine_map[i][j] in symbols_set:
            for k in range(i-1 if i-1 >= 0 else 0, i+2 if i+2 < len(engine_map)+1 else len(engine_map)+1):
                for l in range(j-1 if j-1 >= 0 else 0, j+2 if j+2 < len(engine_map[i])+1 else len(engine_map[i])+1):
                    if engine_map[k][l].isdigit():
                        part_num = engine_map[k][l]
                        left = l-1
                        while left >= 0 and engine_map[k][left].isdigit():
                            part_num = engine_map[k][left] + part_num
                            left -= 1

                        right = l+1
                        while right < len(engine_map[k]) and engine_map[k][right].isdigit():
                            part_num += engine_map[k][right]
                            right += 1

                        found = False
                        for ll in range(len(part_num)):
                            if f"{k}_{l-ll}_{part_num}" in part_set or f"{k}_{l+ll}_{part_num}" in part_set:
                                found = True

                        if not found:
                            part_set.add(f"{k}_{l}_{part_num}")

res = sum(int(part.split('_')[2]) for part in part_set)
print(f"part 1: {res}")

# part 2
res = 0

for i in range(len(engine_map)):
    for j in range(len(engine_map[i])):
        if engine_map[i][j] in symbols_set:
            gears = set()
            for k in range(i-1 if i-1 >= 0 else 0, i+2 if i+2 < len(engine_map)+1 else len(engine_map)+1):
                for l in range(j-1 if j-1 >= 0 else 0, j+2 if j+2 < len(engine_map[i])+1 else len(engine_map[i])+1):
                    if engine_map[k][l].isdigit():
                        part_num = engine_map[k][l]
                        left = l-1
                        while left >= 0 and engine_map[k][left].isdigit():
                            part_num = engine_map[k][left] + part_num
                            left -= 1

                        right = l+1
                        while right < len(engine_map[k]) and engine_map[k][right].isdigit():
                            part_num += engine_map[k][right]
                            right += 1

                        gears.add(f"{k}_{part_num}")

            if engine_map[i][j] == "*" and len(gears) == 2:
                ratio = 1
                for val in gears:
                    ratio *= int(val.split("_")[1])
                res += ratio

print(f"part 2: {res}")
