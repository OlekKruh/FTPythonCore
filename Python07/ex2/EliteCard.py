from ex0 import Card
from .Combatable import Combatable
from .Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack_damage: int, health: int, defense: int):
        super().__init__(name, cost, rarity)
        self.attack_damage = attack_damage
        self.health = health
        self.defense = defense
        self.current_mana = 0

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "effect": "Elite unit entered battlefield"
        }

    def attack(self, target) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.attack_damage,
            "combat_type": "melee"
        }

    def defend(self, incoming_damage: int) -> dict:
        damage_taken = max(0, incoming_damage - self.defense)
        self.health -= damage_taken

        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": self.defense,
            "still_alive": self.health > 0
        }

    def get_combat_stats(self) -> dict:
        return {
            "attack": self.attack_damage,
            "defense": self.defense,
            "health": self.health
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": self.cost,
        }

    def channel_mana(self, amount: int) -> dict:
        self.current_mana += amount
        return {
            "channeled": amount,
            "total_mana": self.current_mana
        }

    def get_magic_stats(self) -> dict:
        return {"current_mana": self.current_mana}
