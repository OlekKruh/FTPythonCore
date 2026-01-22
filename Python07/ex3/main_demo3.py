from ex3 import GameEngine, FantasyCardFactory, AggressiveStrategy


def main():
    print("=== DataDeck Game Engine ===")
    print()

    print("Configuring Fantasy Card Game...")
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    engine = GameEngine()
    engine.configure_engine(factory, strategy)

    print(f"Factory: {type(factory).__name__}")
    print(f"Strategy: {strategy.get_strategy_name()}")
    print(f"Available types: {factory.get_supported_types()}")
    print()
    print("Simulating aggressive turn...")
    engine.simulate_turn()
    print()
    print("Game Report:")
    print(engine.get_engine_status())
    print()
    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
