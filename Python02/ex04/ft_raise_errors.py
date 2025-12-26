def check_plant_health(plant_name: str, water_level: int, sunlight_hours: int) -> None:
    """
    Description:
        Checks the vital parameters of a plant and reports its health status.
        Uses a try-except-else block to validate inputs. If any parameter is invalid,
        it raises and catches a ValueError, printing an error message.
        If all parameters are valid, it prints a success message in the else block.
    Args:
        plant_name (str): The name of the plant (cannot be empty).
        water_level (int): The water level (must be <= 10).
        sunlight_hours (int): Hours of sunlight (must be >= 2).
    Returns:
        None: This function only prints to stdout.
    """
    try:
        if not plant_name:
            raise ValueError("Plant name cannot be empty!\n")
        if water_level > 10:
            raise ValueError(f"Water level {water_level} is too high (max 10)\n")
        if sunlight_hours < 2:
            raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)\n")
    except ValueError as e:
        print(f"Error: {e}")
    else:
        print(f"Plant '{plant_name}' is healthy!\n")


def test_plant_checks() -> None:
    """
    Description:
        Runs a series of tests to demonstrate error handling capabilities.
        Scenarios:
        1. Valid data -> Success message.
        2. Missing name -> ValueError caught.
        3. Excessive water -> ValueError caught.
        4. Insufficient sunlight -> ValueError caught.
    """
    print("Testing good values...")
    check_plant_health("tomato", 8, 5)

    print("Testing empty plant name...")
    check_plant_health(None, 8, 5)

    print("Testing bad water level...")
    check_plant_health("tomato", 15, 5)

    print("Testing bad sunlight hours...")
    check_plant_health("tomato", 8, 0)


if __name__ == "__main__":
    print("=== Garden Plant Health Checker ===\n")
    test_plant_checks()
    print("All error raising tests completed!")
