from .GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        available_mana = 5
        cards_played = []
        mana_used = 0
        damage_dealt = 0

        sorted_hand = sorted(hand, key=lambda x: x.cost)

        for card in sorted_hand:
            if card.cost <= available_mana:
                available_mana -= card.cost
                mana_used += card.cost
                cards_played.append(card.name)

                if hasattr(card, 'attack'):
                    damage_dealt += card.attack
                elif hasattr(card, 'effect_type') and card.effect_type == 'damage':
                    damage_dealt += 3

        return {
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": self.prioritize_targets(["Enemy Player"]),
            "damage_dealt": damage_dealt
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        return ["Enemy Player"]
