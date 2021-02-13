data = input().split()

final = {}

for i in data:
    for j in i:
        if j not in final:
            final[j] = 1
        else:
            final[j] += 1

for word, count in final.items():
    print(f"{word} -> {count}")





