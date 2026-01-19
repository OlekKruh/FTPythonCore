from .validator import validate_ingredients


def record_spell(spell_name: str, ingredients: str) -> str:
    """Register a new spell into the grimoire after validating its ingredients.
    Uses a late import for the validator to prevent circular dependency issues.
    Args:
        spell_name (str): The name of the spell to record.
        ingredients (str): The components required for the spell.
    Returns:
        str: A message confirming if the spell was recorded or rejected based
        on validation.
    """
    validation_result = validate_ingredients(ingredients)
    if validation_result:
        return f"Spell recorded: {spell_name} ({validation_result})"
    else:
        return f"Spell rejected: {spell_name} ({validation_result})"
