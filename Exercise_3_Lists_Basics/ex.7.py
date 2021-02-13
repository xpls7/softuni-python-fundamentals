initial_input = input()
gifts = initial_input.split()

command = input()

while command != "No Money":
    if "OutOfStock" in command:
        gifts = ["None" if x == command.split()[1] else x for x in gifts]
    if "Required" in command and -1 < int(command.split()[2]) < len(gifts):
            gifts[int(command.split()[2])] = command.split()[1]
    if "JustInCase" in command:
        gifts[len(gifts)-1] = command.split()[1]
    command = input()

for gift in gifts:
    if gift !="None":
        print(gift, end=' ')
