import math

num_people = int(input())
capacity = int(input())

full_courses = math.ceil(num_people / capacity)

print(full_courses)

