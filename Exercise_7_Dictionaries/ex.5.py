num = int(input())

users = {}

for n in range(num):
    data = input().split()
    command = data[0]
    name = data[1]


    if command == "register":
        car = data[2]
        if name in users:
            print(f"ERROR: already registered with plate number {car}")
        else:
            users[name] = car
            print(f"{name} registered {car} successfully")
    elif command == "unregister":
        if name not in users:
            print(f"ERROR: user {name} not found")
        else:
            users.pop(name)
            print(f"{name} unregistered successfully")

for name, car in users.items():
    print(f"{name} => {car}")

