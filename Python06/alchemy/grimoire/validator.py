def validate_ingredients(ingredients: str) -> str:
    ingredients_list = ["fire", "water", "earth", "air"]
    if ingredients in ingredients_list:
        return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"