from ex4 import TournamentPlatform, TournamentCard


def main():
    print("=== DataDeck Tournament Platform ===")
    print()

    platform = TournamentPlatform()

    print("Registering Tournament Cards...")
    print()
    dragon = TournamentCard("Fire Dragon", 5, "Legendary", 10, 5)
    wizard = TournamentCard("Ice Wizard", 4, "Epic", 6, 8)

    d_id = platform.register_card(dragon)
    w_id = platform.register_card(wizard)

    print("Creating tournament match...")
    match_res = platform.create_match(d_id, w_id)
    print(f"Match result: {match_res}")
    print()

    print("Tournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    for i, line in enumerate(leaderboard, 1):
        print(f"{i}. {line}")
    print()

    print("Platform Report:")
    print(platform.generate_tournament_report())
    print()

    print("=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
