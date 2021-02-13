data = input()
courses = {}
users = {}
quantity = 0

while not data == "end":
    course, name =  data.split(" : ")

    if course not in courses:
        courses[course] = quantity + 1
        users[name] = course
    else:
        users[name] = course
        courses[course] += 1

    data = input()

for course, quantity in sorted(courses.items(), key=lambda x: -x[1]):
    print(f"{course}: {quantity}")
    for name, data in sorted(users.items(), key=lambda x: x[0]):
        if data == course:
            print(f"-- {name}")

