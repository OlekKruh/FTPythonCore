def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts,
                  key=lambda a: a["power"],
                  reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    max_p_m = max(mages, key=lambda m: m["power"])
    min_p_m = min(mages, key=lambda m: m["power"])
    sum_p = sum(map(lambda m: m["power"], mages))
    avr_p = sum_p/len(mages)
    res = {
        "max_power": max_p_m["power"],
        "min_power": min_p_m["power"],
        "avg_power": avr_p
    }
    return res


def main():
    artifacts = [
        {'name': 'Ice Wand', 'power': 107, 'type': 'focus'},
        {'name': 'Shadow Blade', 'power': 114, 'type': 'relic'},
        {'name': 'Light Prism', 'power': 73, 'type': 'relic'},
        {'name': 'Crystal Orb', 'power': 100, 'type': 'relic'}
    ]
    mages = [
        {'name': 'Riley', 'power': 68, 'element': 'lightning'},
        {'name': 'Riley', 'power': 67, 'element': 'wind'},
        {'name': 'Morgan', 'power': 62, 'element': 'light'},
        {'name': 'Ember', 'power': 56, 'element': 'lightning'},
        {'name': 'Zara', 'power': 69, 'element': 'light'}
    ]
    spells = ['lightning', 'tornado', 'shield', 'meteor']

    n = 25
    print("Testing artifact sorter...")
    print(f"{'Not sorted':<{n}} | {'Sorted':<{n}}")
    print(f"{'Name: Power, Type':<{n}} | {'Name: Power, Type':<{n}}")
    print("=" * n * 2)
    sorted_artifacts = artifact_sorter(artifacts)
    for i in range(len(artifacts)):
        original = artifacts[i]
        ranked = sorted_artifacts[i]
        u_str = f"{original['name']}: {original['power']}, {original['type']}"
        s_str = f"{ranked['name']}: {ranked['power']}, {ranked['type']}"
        print(f"{u_str:<25} | {s_str:<25}")
    print()
    print("Testing power filter...")
    print(f"{'Not sorted':<{n}} | {'Sorted':<{n}}")
    print(f"{'Name: Power, Element':<{n}} | {'Name: Power, Element':<{n}}")
    print("=" * n * 2)
    filtered_mages = power_filter(mages, 65)
    max_len = max(len(mages), len(filtered_mages))
    for i in range(max_len):
        if i < len(mages):
            origin = mages[i]
            u_str = f"{origin['name']}: {origin['power']}, {origin['element']}"
        else:
            u_str = ""
        if i < len(filtered_mages):
            filtr = filtered_mages[i]
            s_str = f"{filtr['name']}: {filtr['power']}, {filtr['element']}"
        else:
            s_str = ""
        print(f"{u_str:<{n}} | {s_str:<{n}}")
    print()
    print("Testing spell transformer...")
    transformed_spells = spell_transformer(spells)
    print(f"{" ".join(transformed_spells)}")
    print()
    print("Testing mage stats...")
    stats = mage_stats(mages)
    for key, value in stats.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
