def calc_factorial(n):
    res = 1
    for num in range (2, n+1):
        res *= num

    return res

num_1 = int(input())
num_2 = int(input())

fact_num_1 = calc_factorial(num_1)
fact_num_2 = calc_factorial(num_2)

result = fact_num_1 / fact_num_2

print(f"{result:.2f}")
