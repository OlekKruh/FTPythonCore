def water_plants(plant_list: list) -> None:
    """
    Description:
        Simulates a watering system with guaranteed resource cleanup.
        Iterates through a list of plants. Uses string concatenation to intentionally
        trigger a TypeError if a plant is None. Uses a 'finally' block to ensure
        the system closes even if a crash occurs.
    Args:
        plant_list (list): A list of plant names (str) or None values.
    Raises:
        TypeError: Caught internally when attempting to concatenate str + None.
    """
    print("Opening watering system")
    try:
        for plant in plant_list:
            print("Watering " + plant)
    except TypeError:
        print("Error: Cannot water None - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    """
    Description:
        Runs tests to demonstrate the 'finally' block behavior.
        Scenarios:
        1. Successful run: All plants are valid strings.
        2. Error run: List contains None, causing a crash midway.
        In both cases, 'Closing watering system' must be printed.
    """
    good_list = ["tomato", "lettuce", "carrots"]
    bad_list = ["tomato", None]

    print("Testing normal watering...")
    water_plants(good_list)
    print("Watering completed successfully!\n")

    print("Testing with error...")
    water_plants(bad_list)


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    test_watering_system()
