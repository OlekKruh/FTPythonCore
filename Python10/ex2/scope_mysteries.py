from typing import Callable, Dict


def mage_counter() -> Callable:
    counter = 0

    def inner_f() -> int:
        nonlocal counter
        counter += 1
        return counter
    return inner_f


def spell_accumulator(initial_power: int) -> Callable:
    accumulator = initial_power

    def power_f(extra_power: int) -> int:
        nonlocal accumulator
        accumulator += extra_power
        return accumulator
    return power_f


def enchantment_factory(enchantment_type: str) -> Callable:
    def apply_enchantment(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return apply_enchantment


def memory_vault() -> Dict[str, Callable]:
    storage = {}

    def store(key: str, value: str):
        storage[key] = value

    def recall(key: str) -> str:
        if key in storage:
            return storage[key]
        else:
            return "Memory not found"

    return {"store": store, "recall": recall}


def main():
    initial_powers = [42, 72, 78]
    power_additions = [7, 8, 8, 16, 15]
    enchantment_types = ['Flowing', 'Radiant', 'Frozen']
    items_to_enchant = ['Wand', 'Cloak', 'Amulet', 'Armor']

    print("\n" + "=" * 50)
    print(f"{'🔮 SCOPE MYSTERIES: DEMONSTRATION':^50}")
    print("=" * 50)

    # --- 1. MAGE COUNTER TEST ---
    print("\n1. TEST: Mage Counter (Closure State)")
    print("-" * 50)

    # Create counter
    counter = mage_counter()
    print("Mage starts casting spells...")

    # 5 calls
    for i in range(5):
        current_count = counter()
        print(f" -> Cast #{i + 1}: Counter returned {current_count}")

    # --- 2. SPELL ACCUMULATOR TEST ---
    print("\n2. TEST: Spell Accumulator (Running Total)")
    print("-" * 50)

    start_power = initial_powers[0]
    print(f"Creating accumulator with Base Power: {start_power}")

    # Create accumulator
    accumulator_func = spell_accumulator(start_power)

    print(f"{'Action':<20} | {'New Total Power':<20}")
    print("-" * 45)

    # Add powers
    for power_up in power_additions:
        new_total = accumulator_func(power_up)
        print(f"Adding +{power_up:<12} | {new_total:<20}")

    # --- 3. ENCHANTMENT FACTORY TEST ---
    print("\n3. TEST: Enchantment Factory (Currying)")
    print("-" * 65)
    print(f"{'Factory Type':<15} | {'Item':<10} | {'Resulting Name':<30}")
    print("-" * 65)

    for ench_type in enchantment_types:
        # Create factory
        current_factory = enchantment_factory(ench_type)

        # Using enchantment
        for item in items_to_enchant:
            full_name = current_factory(item)
            print(f"{ench_type:<15} | {item:<10} | {full_name:<30}")

        print(f"{'-' * 65}")

    # --- 4. MEMORY VAULT TEST ---
    print("\n4. TEST: Memory Vault (Data Hiding)")
    print("-" * 50)

    vault = memory_vault()

    # Add to storage
    print("Storing secrets in the vault...")
    vault['store']("Secret_Code", "777-XYZ")
    vault['store']("Location", "Hidden Tower")
    print(" -> Data stored.")

    print("\nAttempting to recall:")
    # Extract from storage
    keys_to_check = ["Secret_Code", "Location", "Gold_Stash"]

    for key in keys_to_check:
        result = vault['recall'](key)
        status = "✅ FOUND" if result != "Memory not found" else "❌ MISSING"
        print(f"Key: {key:<15} -> Result: {result:<15} ({status})")

    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()
