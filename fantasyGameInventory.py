stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(v,k)
        item_total += v
    print("Total number of items: " + str(item_total))

#displayInventory(stuff)

def addToInventory(inv, addedItems):
    for i in addedItems:
        if i in inv:
            inv[i] += 1
        else:
            inv[i] = 1
    print(inv)


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
