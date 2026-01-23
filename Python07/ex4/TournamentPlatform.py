from ex4 import TournamentCard


class TournamentPlatform:
    def __init__(self):
        self.registry = {}
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        base_id = card.name.split()[0].lower()
        card_id = f"{base_id}_001"

        self.registry[card_id] = card

        print(f"{card.name} (ID: {card_id}):")
        parents = [b.__name__ for b in type(card).__bases__]
        print(f"- Interfaces: {parents}")
        print(f"- Rating: {card.rating}")
        print(f"- Record: {card.wins}-{card.losses}")
        print()

        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        fighter1 = self.registry.get(card1_id)
        fighter2 = self.registry.get(card2_id)

        if not fighter1 or not fighter2:
            return {"error": "Card not found"}

        self.matches_played += 1

        score1 = fighter1.attack_value
        score2 = fighter2.attack_value

        if score1 >= score2:
            winner = fighter1
            loser = fighter2
            winner_id = card1_id
            loser_id = card2_id
        else:
            winner = fighter2
            loser = fighter1
            winner_id = card2_id
            loser_id = card1_id

        winner.update_wins(1)
        loser.update_losses(1)

        return {
            "winner": winner_id,
            "loser": loser_id,
            "winner_rating": winner.calculate_rating(),
            "loser_rating": loser.calculate_rating()
        }

    def get_leaderboard(self) -> list:
        cards = list(self.registry.values())
        sorted_cards = sorted(cards, key=lambda c: c.rating, reverse=True)

        leaderboard = []
        for card in sorted_cards:
            info = (f"{card.name} - Rating: "
                    f"{card.rating} ({card.wins}-{card.losses})")
            leaderboard.append(info)
        return leaderboard

    def generate_tournament_report(self) -> dict:
        total_rating = sum(c.rating for c in self.registry.values())
        count = len(self.registry)
        avg = total_rating / count if count > 0 else 0

        return {
            "total_cards": count,
            "matches_played": self.matches_played,
            "avg_rating": int(avg),
            "platform_status": "active"
        }
