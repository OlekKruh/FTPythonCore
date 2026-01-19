from alchemy.elements import create_fire, create_earth


def lead_to_gold():
    """Transmute lead into gold using elemental fire.
    Returns:
        str: A confirmation message of the metallic transmutation.
    """
    return f"Lead transmuted to gold using {create_fire()}"


def stone_to_gem():
    """Transmute common stone into a precious gem using earth magic.
    Returns:
        str: A confirmation message of the mineral transmutation.
    """
    return f"Stone transmuted to gem using {create_earth()}"
