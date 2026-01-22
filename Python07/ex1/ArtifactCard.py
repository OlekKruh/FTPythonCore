from ex0 import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str) -> None:
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        return {"card_played": self.name, "mana_used": self.cost,
                "effect": self.effect}

    def activate_ability(self) -> dict:
        return {"effect": self.effect}

    def get_card_info(self) -> dict:
        new_dict = super().get_card_info()
        new_dict.update(
            {
                "durability": self.durability,
                "effect": self.effect,
            }
        )
        return new_dict
