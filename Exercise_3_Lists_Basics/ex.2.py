factor = int(input())
count = int(input())

result = []

for i in range(1, count+1):
    i = int(i)
    i = i * factor
    result.append(i)

print(result)
