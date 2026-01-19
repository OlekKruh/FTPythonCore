def validate_ingredients(ingredients: str) -> str:
    """Check if the provided ingredients contain valid elemental components.
    Args:
        ingredients (str): A string listing the ingredients used in the spell.
    Returns:
        str: A status string indicating if the
        ingredients are VALID or INVALID.
    """
    ingredients_list = ["fire", "water", "earth", "air"]
    if ingredients in ingredients_list:
        return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"
