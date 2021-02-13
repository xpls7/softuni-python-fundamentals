rooms_number = int(input())

list_chairs = []

for room in range(1, rooms_number+1):
    chairs = input().split()
    counter = 0

    for chair in chairs[0]:
        counter += 1

    free_chairs = counter - int(chairs[1])

    if free_chairs < 0:
        needed_chairs = free_chairs * (-1)
        list_chairs.append(free_chairs)
        print(f"{needed_chairs} more chairs needed in room {room}")
    else:
        list_chairs.append(free_chairs)

if sum(list_chairs) > 0:
    print(f"Game On, {sum(list_chairs)} free chairs left")




