from .Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int, health: int):
        super().__init__(name, cost, rarity)
        self.attack = attack if attack > 0 else 0
        self.health = health if health > 0 else 0

    def play(self, game_state: dict) -> dict:
        return {"card_played": self.name, "mana_used": self.cost,
                "effect": "Creature summoned to battlefield"}

    def attack_target(self, name: str) -> dict:
        return {"attacker": self.name, "target": name,
                "damage_dealt": self.attack, "combat_resolved": True}

    def get_card_info(self) -> dict:
        base_info = super().get_card_info()
        base_info.update(
            {
                "attack": self.attack,
                "health": self.health,
            }
        )
        return base_info
