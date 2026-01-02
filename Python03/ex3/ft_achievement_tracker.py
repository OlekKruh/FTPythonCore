print("=== Achievement Tracker System ===")
alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
charlie = {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon', 'perfectionist'}

print(f"Player alice achievements: {alice}")
print(f"Player bob achievements: {bob}")
print(f"Player charlie achievements: {charlie}")


print("\n=== Achievement Analytics ===")

uniq = alice.union(bob, charlie)

print(f"All unique achievements: {uniq}")
print(f"Total unique achievements: {len(uniq)}")

common = alice.intersection(bob, charlie)
rare_alice = alice.difference(bob, charlie)
rare_bob = bob.difference(alice, charlie)
rare_charlie = charlie.difference(alice, bob)
rare = rare_alice.union(rare_bob, rare_charlie)

print(f"Common to all players: {common}")
print(f"Rare achievements (1 player): {rare}\n")

alice_bob = alice.intersection(bob)
alice_uniq = alice.difference(bob)
bob_uniq = bob.difference(alice)

print(f"Alice vs Bob common: {alice_bob}")
print(f"Alice unique: {alice_uniq}")
print(f"Bob unique: {bob_uniq}")

# === Achievement Tracker System ===
# Player alice achievements: {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
# Player bob achievements: {'first_kill', 'level_10', 'boss_slayer', 'collector'}
# Player charlie achievements: {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon', 'perfectionist'}

# === Achievement Analytics ===
# All unique achievements: {'boss_slayer', 'collector', 'first_kill', 'level_10', 'perfectionist',
# 'speed_demon', 'treasure_hunter'}
# Total unique achievements: 7

# Common to all players: {'level_10'}
# Rare achievements (1 player): {'collector', 'perfectionist'}

# Alice vs Bob common: {'first_kill', 'level_10'}
# Alice unique: {'speed_demon', 'treasure_hunter'}
# Bob unique: {'boss_slayer', 'collector'}
