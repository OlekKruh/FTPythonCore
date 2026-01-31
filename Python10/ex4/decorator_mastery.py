from typing import Callable, Any
import functools
import time


def spell_timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print(f"Casting {func.__name__}")
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time
        print(f"Spell completed in {duration:.4f} seconds")
        return res
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            power_val = 0
            if 'power' in kwargs:
                power_val = kwargs['power']
            else:
                for arg in args:
                    if isinstance(arg, int):
                        power_val = arg
                        break
            if power_val >= min_power:
                res = func(*args, **kwargs)
                return res
            else:
                return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(f"Spell failed, retrying...\n"
                              f"(attempt {attempt}/{max_attempts})")
                    else:
                        return (f"Spell casting failed after "
                                f"{max_attempts} attempts")
            return "Oops somthing went horribly wrong."
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if all(c.isalpha() or c.isspace() for c in name) and len(name) >= 3:
            return True
        else:
            return False

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with power {power}"


def main():
    test_powers = [23, 8, 15, 9, 17, 30]
    spell_names = ['tornado', 'heal', 'meteor', 'lightning']
    mage_names = ['Nova', 'Jordan', 'Phoenix', 'River', 'Luna', 'Kai']
    invalid_names = ['Jo', 'A', 'Alex123', 'Test@Name']

    mage_guild = MageGuild()

    all_names = mage_names + invalid_names
    print("Testing MageGuild...")
    print(f"{'Mage Name':<15} | {'Status'}:<15")
    print("-" * 30)
    for name in all_names:
        is_valid = mage_guild.validate_mage_name(name)
        status = "Accepted" if is_valid else "Rejected"
        print(f"{name:<15} | {status:<15}")

    print()
    print("=" * 30)
    print("Training ground...")
    print()
    for name, spell, power in zip(mage_names * 2, spell_names * 3, test_powers * 2):
        print(f"Mage {name} try to cast '{spell}' (Power: {power})")
        res = mage_guild.cast_spell(spell_name=spell, power=power)
        if 'Insufficient' in res:
            print(f"   -> Resalt: ⛔ {res}\n")
        else:
            print(f"   -> Resalt: ✅ {res}\n")
    print("End of exercise")


if __name__ == "__main__":
    main()
