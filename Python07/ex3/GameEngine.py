from .CardFactory import CardFactory
from .GameStrategy import GameStrategy


class GameEngine:
    def __init__(self):
        self.factory = None
        self.strategy = None
        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created_count = 0

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        if not self.factory or not self.strategy:
            return {"error": "Engine not configured"}

        hand = [
            self.factory.create_creature("Fire Dragon"),  # Cost 5
            self.factory.create_creature("Goblin Warrior"),  # Cost 2
            self.factory.create_spell("Lightning Bolt")  # Cost 3
        ]
        self.cards_created_count += len(hand)

        hand_str = [f"{c.name} ({c.cost})" for c in hand]
        print(f"Hand: {hand_str}")

        battlefield = []
        turn_result = self.strategy.execute_turn(hand, battlefield)

        self.turns_simulated += 1
        self.total_damage += turn_result.get("damage_dealt", 0)

        print()
        print("Turn execution:")
        print(f"Strategy: {self.strategy.get_strategy_name()}")
        print(f"Actions: {turn_result}")

        return turn_result

    def get_engine_status(self) -> dict:
        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": self.strategy.get_strategy_name()
            if self.strategy else "None",
            "total_damage": self.total_damage,
            "cards_created": self.cards_created_count
        }
