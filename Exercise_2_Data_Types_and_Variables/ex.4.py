num = int(input())
sum = 0

for i in range(1, num + 1):
    char = str(input())
    char_1 = ord(char)
    sum += char_1

print(f"The sum equals: {sum}")
