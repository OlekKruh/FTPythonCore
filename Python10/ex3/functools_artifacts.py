from typing import Callable, List, Dict
import functools
import operator


def spell_reducer(spells: List[int], operation: str) -> int:
    ops = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min,
    }

    if operation not in ops:
        raise ValueError(f"Unknown operation: {operation}")
    selected_func = ops[operation]
    result = functools.reduce(selected_func, spells)
    return result


def partial_enchanter(base_enchantment: Callable) -> Dict[str, Callable]:
    return {
        "fire_enchant": functools.partial(base_enchantment,
                                          power=50,
                                          element="Fire"),
        "ice_enchant": functools.partial(base_enchantment,
                                         power=50,
                                         element="Ice"),
        "lightning_enchant": functools.partial(base_enchantment,
                                               power=50,
                                               element="Lightning"),
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


@functools.singledispatch
def _dispatcher_logic(arg):
    return f"Fizzle... Unknown component {type(arg)}"


@_dispatcher_logic.register(int)
def _(arg: int):
    return f"💥 Dealing {arg} damage"


@_dispatcher_logic.register(str)
def _(arg: str):
    return f"✨ Casting enchantment: {arg}"


@_dispatcher_logic.register(list)
def _(arg: list):
    results = []
    for item in arg:
        results.append(_dispatcher_logic(item))
    return results


def spell_dispatcher() -> Callable:
    return _dispatcher_logic


def main():
    spell_powers = [43, 42, 18, 25, 42, 12]
    operations = ['add', 'multiply', 'max', 'min']
    fibonacci_tests = [17, 15, 16]
    mixed_data = [100, "Invisibility", [10, "Heal"], 50]

    print("\n" + "=" * 50)
    print(f"{'📜 ANCIENT LIBRARY: ARTIFACTS TEST':^50}")
    print("=" * 50)

    # --- 1. TEST: SPELL REDUCER ---
    print("\n1. ARTIFACT: Spell Reducer (Aggregation)")
    print(f"   Input Spells: {spell_powers}")
    print("-" * 50)
    print(f"{'Operation':<15} | {'Result':<20}")
    print("-" * 50)

    for op in operations:
        try:
            result = spell_reducer(spell_powers, op)
            print(f"{op:<15} | {result:<20}")
        except Exception as e:
            print(f"{op:<15} | Error: {e}")

    # --- 2. TEST: MEMOIZED FIBONACCI ---
    print("\n2. ARTIFACT: Memoized Fibonacci (Caching)")
    print("-" * 50)
    print(f"{'N':<10} | {'Fibonacci Number':<20}")
    print("-" * 50)

    for n in fibonacci_tests:
        result = memoized_fibonacci(n)
        print(f"Fib({n})    | {result:<20}")

    # --- 3. TEST: PARTIAL ENCHANTER ---
    print("\n3. ARTIFACT: Partial Enchanter (Config)")
    print("-" * 65)

    def base_spell(target, power, element):
        return f"[{element} Lv.{power}] -> {target}"

    enchant_kit = partial_enchanter(base_spell)

    for enchant_name, func in enchant_kit.items():
        effect = func(target="Mystic Staff")
        print(f"{enchant_name:<20}: {effect}")

    # --- 4. TEST: SPELL DISPATCHER ---
    print("\n4. ARTIFACT: Single Dispatcher (Overloading)")
    print("-" * 50)

    dispatcher = spell_dispatcher()

    for data in mixed_data:
        res = dispatcher(data)
        print(f"Input: {str(data):<20} -> {res}")

    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()
