users = input().split(', ')

for user in users:
    counter = 0
    if len(user) in range(3, 17):
        if user.isalnum():
            print(user)
        else:
            for letter in user:
                if letter.isdigit():
                    counter += 1
                elif letter.isalpha():
                    counter += 1
                elif letter == '-' or letter == '_':
                    counter += 1
            if counter == len(user):
                print(user)
