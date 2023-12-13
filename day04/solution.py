import os
import re

data = []
res = 0

# part 1
with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "input.txt"), "r") as file:
    data = file.readlines()

for d in data:
    score = 0
    winning_numbers = re.split('[:|]', d.strip())[1].split()
    d = re.split('[:|]', d.strip())[2].split()

    for n in d:
        if n in winning_numbers:
            if score == 0:
                score += 1
            else:
                score *= 2
    res += score

print(f"part 1: {res}")

# part 2
copies = {}
with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "input.txt"), "r") as file:
    data = file.readlines()

for d in data:
    winners = 0
    card_num = re.split('[:|]', d.strip())[0].split()[1]
    if not copies.get(f"{int(card_num)}", None):
        copies[f"{int(card_num)}"] = 1
    else:
        copies[f"{int(card_num)}"] += 1
    winning_numbers = re.split('[:|]', d.strip())[1].split()
    d = re.split('[:|]', d.strip())[2].split()

    for n in d:
        if n in winning_numbers:
            winners += 1

    for j in range(1, winners+1):
        if copies.get(f"{int(card_num)+j}", None):
            copies[f"{int(card_num)+j}"] += copies[f"{int(card_num)}"]
        else:
            copies[f"{int(card_num)+j}"] = copies[f"{int(card_num)}"]

print(f"part 2: {sum(copies.values())}")
