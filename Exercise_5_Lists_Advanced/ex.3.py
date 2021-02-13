version = input().split(".")
version = [int(el) for el in version]


for index in version:
    if version[2] < 9:
        version[2] += 1
        break
    else:
        if version[1] < 9:
            version[1] += 1
        else:
            version[1] -= 9
            version[0] += 1
        version[2] -= 9

        break

print('.'.join(map(str, version)))
