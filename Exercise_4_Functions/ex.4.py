def sum_of_all(number):
    sum_even = 0
    sum_odd = 0

    for i in number:
        i = int(i)
        if i % 2 == 0:
            sum_even += i
        else:
            sum_odd += i
    print(f"Odd sum = {sum_odd}, Even sum = {sum_even}")

num = input()

sum_of_all(num)
