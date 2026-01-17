import random
from ex0.Card import Card


class Deck:
    def __init__(self) -> None:
        self.deck = []

    def add_card(self, card: Card) -> None:
        self.deck.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.deck:
            if card.name == card_name:
                self.deck.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.deck)

    def draw_card(self) -> Card:
        if len(self.deck) == 0:
            return None
        return self.deck.pop(0)

    def get_deck_stats(self) -> dict:
        cards_in_deck = len(self.deck)
        creatures = 0
        spells = 0
        artifacts = 0
        total_cost = 0

        for card in self.deck:
            total_cost += card.cost

            card_type = type(card).__name__
            if card_type == "CreatureCard":
                creatures += 1
            elif card_type == "SpellCard":
                spells += 1
            elif card_type == "ArtifactCard":
                artifacts += 1

        avr_cost = total_cost / cards_in_deck if cards_in_deck > 0 else 0

        return {
            "total_cards": cards_in_deck,
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "avg_cost": round(avr_cost, 1)
        }
