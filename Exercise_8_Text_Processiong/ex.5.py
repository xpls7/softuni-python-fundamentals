line = input()

for index in range(len(line)):
    if line[index] == ":":
        print(f"{line[index]}{line[index+1]}")
