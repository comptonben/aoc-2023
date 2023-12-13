import os

data = []
maps = {}
res = 0

# part 1
with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "input.txt"), "r") as file:
    data = file.readlines()

seeds = data[0].split(':')[1].strip().split()

current_map = ""
for d in data[1:]:
    if "map" in d:
        current_map = d.split()[0].strip()
        continue

    if "\n" != d:
        if not maps.get(current_map, None):
            maps[current_map] = []

        maps[current_map].append((int(d.strip().split()[0]), int(d.strip().split()[1]), int(d.strip().split()[2])))

seed_mins = []
for seed in map(int, seeds):
    for m in maps.keys():
        for entry in maps[m]:
            dest_start, src_start, map_size = entry
            src_end = src_start + map_size
            if src_start <= seed < src_end:
                seed = seed - src_start + dest_start
                break
    seed_mins.append(seed)

print(f"part 1: {min(seed_mins)}")

# part 2
seed_tuples = list(zip(seeds[::2], seeds[1::2]))

seed_mins = []
for start, size in seed_tuples:
    seeds = [(int(start), int(start)+int(size))]
    for m in maps.keys():
        changed = []
        for entry in maps[m]:
            dest_start, src_start, map_size = entry
            src_end = src_start + map_size
            unchanged = []
            while seeds:
                seed_start, seed_end = seeds.pop()
                left = (seed_start, min(seed_end, src_start))
                inter = (max(seed_start, src_start), min(src_end, seed_end))
                right = (max(src_end, seed_start), seed_end)
                if left[1] > left[0]:
                    unchanged.append(left)
                if inter[1] > inter[0]:
                    changed.append((inter[0]-src_start+dest_start, inter[1]-src_start+dest_start))
                if right[1] > right[0]:
                    unchanged.append(right)
            seeds = unchanged
        seeds = changed + seeds
    seed_mins.append(min(seeds)[0])

print(f"part 2: {min(seed_mins)}")
