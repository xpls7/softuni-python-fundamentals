class Backpack:
    def __init__(self, backpack: list):
        self.inventory = backpack

    def get(self):
        return self.inventory


class Item:
    def __init__(self, backpack: Backpack, item: str):
        self.backpack = backpack
        self.item = item

    def is_in_backpack(self, item=None):
        if item:
            return item in self.backpack.inventory

        return self.item in self.backpack.inventory

    def collect(self):
        if not self.is_in_backpack():
            self.backpack.inventory.append(self.item)

        return self.backpack

    def drop(self):
        if self.is_in_backpack():
            self.backpack.inventory.remove(self.item)

        return self.backpack

    def combine(self):
        old_item, new_item = self.item.split(':')

        if self.is_in_backpack(old_item):
            self.backpack.inventory.insert(self.backpack.inventory.index(old_item) + 1, new_item)

        return self.backpack

    def renew(self):
        if self.is_in_backpack():
            self.backpack.inventory.append(self.backpack.inventory.pop(self.backpack.inventory.index(self.item)))

        return self.backpack


inventory = Backpack(input().split(', '))
command = input()

while not command == 'Craft!':
    action, items = command.split(' - ')

    inventory_item = Item(inventory, items)

    # Sanitize and format the action to match method name in Item class.
    action = action.split()[0].lower()

    inventory = getattr(inventory_item, action)()

    command = input()

print(', '.join(inventory.get()))
