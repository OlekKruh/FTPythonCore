from .basic import lead_to_gold
from ..potions import healing_potion


def philosophers_stone():
    """Synthesize the legendary Philosopher's Stone.
    Combines the results of gold transmutation and healing potions.
    Returns:
        str: A detailed description of the synthesis process.
    """
    return (f"Philosopher’s stone created using "
            f"{lead_to_gold()} and {healing_potion()}")


def elixir_of_life():
    """Brew the Elixir of Life for eternal youth.
    Returns:
        str: A declaration of the elixir's successful creation.
    """
    return "Elixir of life: eternal youth achieved!"
