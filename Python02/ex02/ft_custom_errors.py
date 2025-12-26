class GardenError(Exception):
    """
    Description:
        Base class for all garden-related exceptions.
    """
    pass


class PlantError(GardenError):
    """
    Description:
        Exception raised when a plant has health issues.
    """
    pass


class WaterError(GardenError):
    """
    Description:
        Exception raised when there are water supply issues.
    """
    pass


def check_plant(name: str, hp: int, water_lvl: int) -> None:
    """
    Description:
        Checks the plant's condition and raises specific exceptions based on issues.
        Logic:
        1. Checks for critical failure (low HP AND low water). Raises GardenError with
           a split-formatted message.
        2. Checks for low HP. Raises PlantError.
        3. Checks for low water. Raises WaterError.
    Args:
        name (str): The name of the plant.
        hp (int): The health points of the plant (0-100).
        water_lvl (int): The current water level (0-100).
    Raises:
        GardenError: If both health and water levels are critically low.
        PlantError: If only health is low (< 50).
        WaterError: If only water is low (< 15).
    """
    if hp < 50 and water_lvl < 15:
        raise GardenError(f"The {name} plant is wilting!|Not enough water in the tank!\n")
    elif hp < 50:
        raise PlantError(f"The {name} plant is wilting!\n")
    elif water_lvl < 15:
        raise WaterError("Not enough water in the tank!\n")


def main():
    """
    Description:
        Runs test scenarios to demonstrate custom exception handling and inheritance.
    """
    print("Testing PlantError...")
    try:
        check_plant("tomato", 34, 25)
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("Testing PlantError...")
    try:
        check_plant("tomato", 55, 2)
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("Testing catching all garden errors...")
    try:
        check_plant("tomato", 10, 2)
    except GardenError as e:
        error_lines = str(e).split('|')
        for line in error_lines:
            print(f"Caught a garden error: {line}")

    print("All custom error types work correctly!")


if __name__ == "__main__":
    main()
