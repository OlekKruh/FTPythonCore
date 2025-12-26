def check_temperature(temp_str: str):
    """
    Description:
        Validates and checks the temperature input for the garden.
        First, attempts to convert the string input to an integer.
        If successful, checks if the temperature is within the safe range (0-40).
        If conversion fails, catches the ValueError.
    Args:
        temp_str (str): The temperature input as a string (e.g., "25", "abc").
    Returns:
        Optional[int]: Returns the temperature as an int if valid and within range.
                       Returns None if invalid or out of range.
    """
    print(f"Testing temperature: {temp_str}")
    try:
        current_temp = int(temp_str)

        if 0 <= current_temp <= 40:
            print(f"Temperature {current_temp}°C is perfect for plants!\n")
            return current_temp
        elif current_temp < 0:
            print(f"Error: {current_temp}°C is too cold for plants (min 0°C)\n")
        else:
            print(f"Error: {current_temp}°C is too hot for plants (max 40°C)\n")

    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")


def test_temperature_input() -> None:
    """
    Description:
        Runs a series of tests with valid and invalid temperature inputs.
        Scenarios:
        1. Valid range ("25") -> Success.
        2. Invalid format ("abc") -> ValueError caught.
        3. Out of range high ("100") -> Logic error printed.
        4. Out of range low ("-50") -> Logic error printed.
    """
    print("=== Garden Temperature Checker ===\n")

    check_temperature("25")
    check_temperature("abc")
    check_temperature("100")
    check_temperature("-50")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
