substring = input().split(", ")
words = input().split(", ")

result = [subst for subst in substring  for word in words if subst in word]
print(sorted(set(result), key=result.index))
