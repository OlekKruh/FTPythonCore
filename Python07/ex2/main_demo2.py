import inspect
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.EliteCard import EliteCard
from ex2.Magical import Magical


arcane_warrior = EliteCard(
        name="Arcane Warrior",
        cost=5,
        rarity="Epic",
        attack_damage=5,
        health=10,
        defense=3
    )


def main():
    print("=== DataDeck Ability System ===")
    print()
    print("EliteCard capabilities:")
    card_methods = [name for name, value in inspect.getmembers(Card, inspect.isfunction)]
    print(f"- Card: {card_methods[1:]}")
    combat_card = [name for name, value in inspect.getmembers(Combatable, inspect.isfunction)]
    print(f"- Combatable: {combat_card[0:]}")
    magic_card = [name for name, value in inspect.getmembers(Magical, inspect.isfunction)]
    print(f"- Magical: {magic_card[0:]}")
    print()
    print(f"Playing {arcane_warrior.name} (Elite Card):")
    print()
    print("Combat phase:")
    attack_res = arcane_warrior.attack("Enemy")
    print(f"Attack result: {attack_res}")
    defend_res = arcane_warrior.defend(5)
    print(f"Defense result: {defend_res}")
    print()
    print("Magic phase:")
    spell_res = arcane_warrior.cast_spell("Fireball", ["Enemy1", "Enemy2"])
    print(f"Spell cast: {spell_res}")
    arcane_warrior.channel_mana(4)
    channel_res = arcane_warrior.channel_mana(3)
    print(f"Mana channel: {channel_res}")
    print()
    print("Multiple interface implementation successful!")


if __name__ == "__main__":
    main()
