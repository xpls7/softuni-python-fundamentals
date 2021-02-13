data = input().split()

data.sort(key=lambda x: len(x))
result = 0

for index in range(len(data[0])):
    result += ord(data[0][index]) * ord(data[1][index])

lefted_letters = sum([ord(letter) for letter in data[1][len(data[0]):]])

print(f'{result + lefted_letters}')






