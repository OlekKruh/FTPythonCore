from .elements import create_fire, create_water, create_air, create_earth


def healing_potion():
    """Combine Fire and Water elements to create a healing elixir.
    Returns:
        str: A description of the potion and its ingredients.
    """
    return f"Healing potion brewed with {create_fire()} and {create_water()}"


def strength_potion():
    """Combine Earth and Fire elements to brew a potion of strength.
    Returns:
        str: A description of the potion and its ingredients.
    """
    return f"Strength potion brewed with {create_earth()} and {create_fire()}"


def invisibility_potion():
    """Combine Air and Water elements to create an invisibility mixture.
    Returns:
        str: A description of the potion and its ingredients.
    """
    return (f"Invisibility potion brewed with {create_air()}"
            f"and {create_water()}")


def wisdom_potion():
    """Combine all four elements to brew the ultimate potion of wisdom.
    Returns:
        str: A description of the potion listing all elemental ingredients.
    """
    return (f"Wisdom potion brewed with all elements: {create_fire()},"
            f"{create_water()}, {create_air()} and {create_earth()} ")
