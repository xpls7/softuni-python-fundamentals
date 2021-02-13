numbers = input().split()


def numbers_as_string(new_list):
    result = int("".join(map(str, new_list)))
    return result


numbers = [int(num) for num in numbers]
new_list = list(reversed(numbers))


print(numbers_as_string(new_list))
