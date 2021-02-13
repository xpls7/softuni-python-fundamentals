line = input()

for letter in line:
    letter = chr(ord(letter) + 3)
    print(letter, end = "")
