from ex0.Card import Card


class SpellCard(Card):
    effect_list = ["damage", "heal", "buff", "debuff"]

    def __init__(self, name: str, cost: int, rarity: str, effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type if effect_type in self.effect_list else "Unknown"

    def play(self, game_state: dict) -> dict:
        return {"card_played": self.name, "mana_used": self.cost,
                "effect": f"Deal {self.cost} damage to target"}

    def resolve_effect(self, targets: list) -> dict:
        targets_str = ", ".join(targets)
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': f'Deal {self.cost} {self.effect_type} to {targets_str}'
        }

    def get_card_info(self) -> dict:
        new_dict = super().get_card_info()
        new_dict.update(
            {
                "effect": self.effect_type,
            }
        )
        return new_dict
