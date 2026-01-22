from ex0 import Card, CreatureCard
from ex1 import SpellCard, ArtifactCard
from tools.card_generator import CardGenerator
from .CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    def __init__(self):
        self.generator = CardGenerator()

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        name = (name_or_power if isinstance(name_or_power, str)
                else "Goblin Warrior")
        data = self.generator.get_creature(name)
        return CreatureCard(**data)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        name = (name_or_power if isinstance(name_or_power, str)
                else "Lightning Bolt")
        data = self.generator.get_spell(name)
        return SpellCard(**data)

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        name = (name_or_power if isinstance(name_or_power, str)
                else "Mana Crystal")
        data = self.generator.get_artifact(name)
        return ArtifactCard(**data)

    def create_themed_deck(self, size: int) -> list:
        deck = []
        for _ in range(size):
            if len(deck) % 3 == 0:
                deck.append(self.create_creature("Fire Dragon"))
            elif len(deck) % 3 == 1:
                deck.append(self.create_spell("Fireball"))
            else:
                deck.append(self.create_artifact("Mana Ring"))
        return deck

    def get_supported_types(self) -> dict:
        return {
            'creatures': ['dragon', 'goblin'],
            'spells': ['fireball', 'lightning bolt'],
            'artifacts': ['mana_ring']
        }
