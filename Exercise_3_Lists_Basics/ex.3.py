cards = input().split()

set_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
set_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

players_a = 11
players_b = 11

for card in cards:
    team, num = card.split("-")
    num = int(num)
    
    if team == "A" and num in set_1:
        set_1.remove(num)
        players_a -= 1
        if players_a < 7:
            break
    elif team == "B" and num in set_2:
        set_2.remove(num)
        players_b -= 1
        if players_b < 7:
            break

print(f"Team A - {players_a}; Team B - {players_b}")

if players_a < 7 or players_b < 7:
    print("Game was terminated")



