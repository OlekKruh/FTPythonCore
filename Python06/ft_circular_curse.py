from alchemy.grimoire import validate_ingredients, record_spell

print("=== Circular Curse Breaking ===")
print()
print("Testing ingredient validation:")
print(f"validate_ingredients(\"fire air\"): {validate_ingredients("fire air")}")
print(f"validate_ingredients(\"dragon scalesf\"): {validate_ingredients("dragon scales")}")
print()
print("Testing spell recording with validation:")
print(f"record_spell(\"Fireball\", \"fire air\"):"
      f"{record_spell("Fireball", "fire air")}")
print(f"record_spell(\"Dark Magic\", \"shadowf\"): "
      f"{record_spell("Dark Magic", "shadowf")}")
print()
print("Testing late import technique:")


from alchemy.grimoire import record_spell as rec
print(f"record_spell(\"Lightning\", \"air\"): "
      f"{rec("Lightning", "air")}")
print()
print("Circular dependency curse avoided using late imports!\n"
      "All spells processed safely!")
