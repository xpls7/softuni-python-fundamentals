num = int(input())


full_tank = 255
watter_all = 0

for i in range(num):
    watter_in = int(input())
    watter_all += watter_in

    if watter_all > full_tank:
        print("Insufficient capacity!")
        watter_all -= watter_in
        continue

print(watter_all)







