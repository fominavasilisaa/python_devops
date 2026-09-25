def clone_inventory(items: list[str]) -> list[str]:
    return items.copy()

bag = ["меч"]
clone = bag
coins = 10
clone_coins = coins
clone.append("утка")
clone_coins += 5
print(bag)
print(bag is clone)
print(coins, clone_coins)