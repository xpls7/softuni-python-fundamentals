n = int(input())

a_small_letter_ascii = ord('a')

for first_char in range(a_small_letter_ascii, a_small_letter_ascii + n):
    for second_char in range(a_small_letter_ascii, a_small_letter_ascii + n):
        for third_char in range(a_small_letter_ascii, a_small_letter_ascii + n):
            print(f"{chr(first_char)}{chr(second_char)}{chr(third_char)}")
