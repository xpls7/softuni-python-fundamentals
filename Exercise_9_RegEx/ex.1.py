import re

line = input()
patter = r"\d+"
numbers = []

while line:
    match = re.findall(patter, line)
    if match:
        numbers.extend(match)

    line = input()

print(" ".join(numbers))
