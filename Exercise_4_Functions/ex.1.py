def smallest(fir, sec, thr):
    if fir < sec and fir < thr:
        return fir
    elif sec < fir and sec < thr:
        return sec
    else:
        return thr

first = int(input())
second = int(input())
third = int(input())

smallest(first, second, third)
print(smallest(first, second, third))
