from CreatureCard import CreatureCard
from tools import CardGenerator

generator = CardGenerator()
fire_dragon = generator.get_creature("Fire Dragon")
goblin_warrior = generator.get_creature("Goblin Warrior")

fire_dragon = CreatureCard(**fire_dragon)
goblin_warrior = CreatureCard(**goblin_warrior)

game_table = {}

print("=== DataDeck Card Foundation ===")
print()
print("Testing Abstract Base Class Design:")
print("CreatureCard Info:")
print(fire_dragon.get_card_info())
print()
print(f"Playing {fire_dragon.name} with {fire_dragon.cost} mana available:")
print(f"Playable: {fire_dragon.is_playable(fire_dragon.cost)}")
print(f"Play result: {fire_dragon.play(game_table)}")
print()
print("Fire Dragon attacks Goblin Warrior:")
print(f"Attack result: {fire_dragon.attack_target(goblin_warrior.name)}")
print()
low_mana = 2
print(f"Testing insufficient mana ({low_mana} available):")
print(f"Playable: {fire_dragon.is_playable(low_mana)}")
print()
print("Abstract pattern successfully demonstrated!")
