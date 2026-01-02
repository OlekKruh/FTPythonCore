alice = {
    "sword": {"type": "weapon", "rarity": "rare", "qty": 1, "price": 500},
    "magic_ring": {"type": "jewelry", "rarity": "epic", "qty": 1, "price": 1000},
    "potion": {"type": "consumable", "rarity": "common", "qty": 4, "price": 50},
    "shield": {"type": "armor", "rarity": "uncommon", "qty": 1, "price": 200}
}
bob = {
    "magic_ring": {"type": "accessory", "rarity": "rare", "qty": 1, "price": 150}
}
total_val = 0
total_count = 0

print("=== Player Inventory System ===\n")
print("=== Alice's Inventory ===")

for name, data in alice.items():
    item_total = data["qty"] * data["price"]

    total_val += item_total
    total_count += data["qty"]

    print(f"{name} ({data['type']}, {data['rarity']}): {data['qty']}x @ {data['price']} gold each = {item_total} gold")

print("")
print(f"Inventory value: {total_val} gold")
print(f"Item count: {total_count} items")
print(f"Categories: weapon({alice['sword']['qty']}),"
      f" consumable({alice['potion']['qty']}),"
      f" armor({alice['shield']['qty']})")

# ===================
print("\n=== Transaction: Alice gives Bob 2 potions ===")

alice["potion"]["qty"] -= 2

if "potion" in bob:
    bob["potion"]["qty"] = bob["potion"]["qty"] + 2
else:
    bob["potion"] = {"type": "consumable", "rarity": "common", "qty": 2, "price": 50}

print("Transaction successful!")

print("\n=== Updated Inventories ===")
print(f"Alice potions: {alice['potion']['qty']}")
print(f"Bob potions: {bob['potion']['qty']}")

print("\n=== Inventory Analytics ===")

alice_gold = 0
for v in alice.values():
    alice_gold = alice_gold + (v["qty"] * v["price"])

bob_gold = 0
for v in bob.values():
    bob_gold = bob_gold + (v["qty"] * v["price"])

if alice_gold > bob_gold:
    print(f"Most valuable player: Alice ({alice_gold} gold)")
else:
    print(f"Most valuable player: Bob ({bob_gold} gold)")

alice_cnt = 0
for v in alice.values():
    alice_cnt += v["qty"]
print(f"Most items: Alice ({alice_cnt} items)")

alice_rar = ""
for key, value in alice.items():
    if value['rarity'] == "epic":
        alice_rar = key

if not alice_rar:
    print("Rarest items: None")
else:
    print(f"Rarest items: {alice_rar}")
