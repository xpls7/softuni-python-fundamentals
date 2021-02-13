
def all_symbol(ch_1, ch_2):
    for i in range((ord(char_1))+1, ord(ch_2)):
        print(chr(i), end=" ")

char_1 = input()
char_2 = input()

all_symbol(char_1, char_2)
