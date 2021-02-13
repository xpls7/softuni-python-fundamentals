items = input().split("|")
budjet = float(input())

bought_items = []
overall_profit = 0.0


for item in items:
    item_type, item_price = item.split("->")
    item_price = float(item_price)

    if item_type == "Clothes" and item_price > 50:
        continue
    elif item_type == "Shoes" and item_price > 35:
        continue
    elif item_type == "Accessories" and item_price > 20.50:
        continue

    if budjet >= item_price:
        budjet -= item_price
        current_profit = item_price * 0.40
        overall_profit += current_profit
        bought_items.append(item_price + current_profit)

for el in bought_items:
    print(f"{el:.2f} ", end='')
print()
print(f"Profit: {overall_profit:.2f}")

budjet += sum(bought_items)

if budjet >= 150:
    print("Hello, France!")
else:
    print("Time to go.")
