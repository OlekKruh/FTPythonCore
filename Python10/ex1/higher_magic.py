from typing import Callable, List


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def wrapper(*args):
        res1 = spell1(*args)
        res2 = spell2(*args)
        return res1, res2
    return wrapper


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def wrapper(*args):
        base_res = base_spell(*args)
        return base_res * multiplier
    return wrapper


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def wrapper(*args):
        if condition(*args):
            return spell(*args)
        else:
            return "Spell fizzled"
    return wrapper


def spell_sequence(spells: List[Callable]) -> Callable:
    def wrapper(*args):
        results = []
        for spell in spells:
            res = spell(*args)
            results.append(res)
        return results
    return wrapper


def main():
    # Basic Spells
    def cast_fireball(target):
        return f"🔥 Fireball -> {target}"

    def cast_ice_shard(target):
        return f"❄️ Ice Shard -> {target}"

    def cast_curse(target):
        return f"💀 Curse -> {target}"

    def base_damage(power):
        return power

    # Generated Data
    test_values = [8, 24, 21]
    test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']

    print("\n" + "=" * 60)
    print(f"{'🧙 MAGICAL SYSTEM SHOWCASE':^60}")
    print("=" * 60 + "\n")

    # --- 1. TEST: SPELL COMBINER ---
    print("1. SPELL COMBINER (Fire + Ice)")
    print("-" * 65)
    print(f"{'Target':<10} | {'Result Tuple (Fire, Ice)':<50}")
    print("-" * 65)

    fire_and_ice = spell_combiner(cast_fireball, cast_ice_shard)

    for target in test_targets:
        result = fire_and_ice(target)
        res_str = f"{result[0]}, {result[1]}"
        print(f"{target:<10} | {res_str:<50}")
    print("\n")

    # --- 2. TEST: POWER AMPLIFIER ---
    print("2. POWER AMPLIFIER (Multiplier: x10)")
    print("-" * 45)
    print(f"{'Input Power':<15} | {'Amplified Result':<20}")
    print("-" * 45)

    amplifier = power_amplifier(base_damage, 10)

    for val in test_values:
        result = amplifier(val)
        print(f"{val:<15} | {result:<20}")
    print("\n")

    # --- 3. TEST: CONDITIONAL CASTER ---
    print("3. CONDITIONAL CASTER (Condition: Power > 20)")
    print("-" * 45)
    print(f"{'Input Power':<15} | {'Cast Result':<25}")
    print("-" * 45)

    high_power_spell = conditional_caster(lambda x: x > 20, base_damage)

    for val in test_values:
        result = high_power_spell(val)
        print(f"{val:<15} | {result:<25}")
    print("\n")

    # --- 4. TEST: SPELL SEQUENCE ---
    print("4. SPELL SEQUENCE (Fire -> Ice -> Curse)")
    print("-" * 80)
    print(f"{'Target':<10} | {'Full Sequence List':<65}")
    print("-" * 80)

    ultimate_combo = spell_sequence([
        cast_fireball,
        cast_ice_shard,
        cast_curse
    ])

    for target in test_targets:
        result_list = ultimate_combo(target)
        print(f"{target:<10} | {str(result_list):<65}")
    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
