from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck
from tools.card_generator import CardGenerator


generator = CardGenerator()
deck = Deck()
game_state = {}

c_card = generator.get_creature("Fire Dragon")
s_card = generator.get_spell("Lightning Bolt")
a_card = generator.get_artifact("Mana Crystal")

c_card = CreatureCard(**c_card)
s_card = SpellCard(**s_card)
a_card = ArtifactCard(**a_card)

deck.add_card(c_card)
deck.add_card(s_card)
deck.add_card(a_card)

print("=== DataDeck Deck Builder ===")
print()
print("Building deck with different card types...")
print(f"Deck stats: {deck.get_deck_stats()}")
print()
print("Drawing and playing cards:")
print()

for _ in range(3):
    card = deck.draw_card()
    if card:
        type_name = type(card).__name__.replace("Card", "")
        print(f"Drew: {card.name} ({type_name})")
        print(f"Play result: {card.play(game_state)}")
    print()

print("Polymorphism in action: Same interface, different card behaviors!")
