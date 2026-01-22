from ex0 import Card
from ex2 import Combatable
from .Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int,
                 rarity: str, attack_value: int, defense_value: int):
        super().__init__(name, cost, rarity)

        self.attack_value = attack_value
        self.defense_value = defense_value

        self.wins = 0
        self.losses = 0
        self.rating = 1150 if "Wizard" in name else 1200

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "effect": "Entered tournament arena"
        }

    def attack(self, target) -> dict:
        return {
            "attacker": self.name,
            "damage": self.attack_value
        }

    def defend(self, incoming_damage: int) -> dict:
        damage_taken = max(0, incoming_damage - self.defense_value)
        return {
            "defender": self.name,
            "damage_taken": damage_taken
        }

    def get_combat_stats(self) -> dict:
        return {"attack": self.attack_value, "defense": self.defense_value}

    def calculate_rating(self) -> int:
        return self.rating

    def update_wins(self, amount: int = 1) -> None:
        self.wins += amount
        self.rating += 16

    def update_losses(self, amount: int = 1) -> None:
        self.losses += amount
        self.rating -= 16

    def get_rank_info(self) -> dict:
        return {
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses
        }

    def get_tournament_stats(self) -> dict:
        return {
            "name": self.name,
            "rating": self.rating,
            "record": f"{self.wins}-{self.losses}"
        }
