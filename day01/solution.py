import os

data = []
first_digit = ''
last_digit = ''
sum = 0

# part 1
with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "input.txt"), "r") as file:
    data = file.readlines()

for d in data:
    for c in d:
        if c.isdigit():
            first_digit = c
            break

    for c in d[::-1]:
        if c.isdigit():
            last_digit = c
            break

    sum += int(first_digit+last_digit)

print(f"part 1: {sum}")

# part 2
sum = 0
with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "input.txt"), "r") as file:
    data = file.readlines()

num_replace = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

for num in num_replace.keys():
    for i, d in enumerate(data):
        _d = d.replace(num, f"{num}{num_replace[num]}{num}")
        data[i] = _d

for d in data:
    for c in d:
        if c.isdigit():
            first_digit = c
            break

    for c in d[::-1]:
        if c.isdigit():
            last_digit = c
            break

    sum += int(first_digit+last_digit)

print(f"part 2: {sum}")
