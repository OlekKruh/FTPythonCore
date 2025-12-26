class Plant:
    """
    Description:
        Represents a plant in the garden.
    Attributes:
        name (str): The name of the plant.
        water_lvl (int): The current water level of the plant.
        sunlight_h (int): The number of sunlight hours the plant receives.
    """
    def __init__(self, name: str, water_lvl: int, sunlight_h: int) -> None:
        self.name = name
        self.water_lvl = water_lvl
        self.sunlight_h = sunlight_h


class GardenError(Exception):
    """Base class for exceptions in the Garden module."""


class GardenManager:
    """
    Description:
       Manages a collection of plants and garden operations.

    Attributes:
        plants (list): A list of Plant objects in the garden.
        MAX_WATER (int): The maximum allowed water level.
        MIN_SUN (int): The minimum required sunlight hours.
    """
    def __init__(self) -> None:
        """
        Description:
            Initializes the GardenManager with empty plant list and constraints.
        """
        self.plants = []
        self.MAX_WATER = 10
        self.MIN_SUN = 2

    def add_plant(self, plant: Plant) -> None:
        """
        Description:
            Adds a plant to the garden if it passes the status check.
        Args:
            plant (Plant): The plant object to be added.
        Raises:
            ValueError: Caught internally if the plant fails validation.
        """
        try:
            if self.plant_status_check(plant):
                self.plants.append(plant)
                print(f"Added {plant.name} successfully")
        except ValueError as e:
            print(f"Error adding plant: {e}")

    def plant_status_check(self, plant: Plant) -> bool:
        """
        Description:
            Validates the plant's vital statistics.
        Args:
            plant (Plant): The plant object to check.
        Returns:
            bool: True if the plant is valid.
        Raises:
            ValueError: If plant name is empty, water is too high, or sun is too low.
        """
        if not plant.name:
            raise ValueError("Plant name cannot be empty!\n")
        if plant.water_lvl > self.MAX_WATER:
            raise ValueError(f"Water level {plant.water_lvl} is too high (max 10)\n")
        if plant.sunlight_h < self.MIN_SUN:
            raise ValueError(f"Sunlight hours {plant.sunlight_h} is too low (min 2)\n")
        return True

    def water_plants(self) -> None:
        """
        Description:
            Waters all plants in the garden.
            Demonstrates error handling when encountering a plant with an invalid name (None).
            Captures TypeError specifically for string concatenation errors.
        """
        print("Opening watering system")
        try:
            for plant in self.plants:
                print("Watering " + plant.name + "- success")
        except TypeError:
            print("Error: Cannot water None - invalid plant!")
        finally:
            print("Closing watering system (cleanup)\n")

    def check_plant_health(self, plant: Plant) -> None:
        """
        Description:
            Checks the health of a specific plant based on garden constraints.
        Args:
            plant (Plant): The plant to check.
        Raises:
            GardenError: If conditions are not met (caught internally).
        """
        try:
            if plant.sunlight_h < self.MIN_SUN and plant.water_lvl < self.MAX_WATER:
                raise GardenError(f"The {plant.name} plant is wilting and not enough water in the tank!")
            elif plant.sunlight_h < self.MIN_SUN:
                raise GardenError(f"The {plant.name} plant is wilting!")
            elif plant.water_lvl < self.MAX_WATER:
                raise GardenError("Not enough water in the tank!")
            else:
                print(f"{plant.name}: healthy (water: {plant.water_lvl}, sun: {plant.sunlight_h})")
        except GardenError as e:
            print(f"Caught Garden Error: {e}")
        finally:
            print("System recovered and continuing...\n")


if __name__ == "__main__":
    print("=== Garden Management System ===\n")
    manager = GardenManager()
    tomato = Plant("tomato", 3, 6)
    lettuce = Plant("lettuce", 1, 6)
    unknown = Plant(None, 0, 0)
    print("Adding plants to garden...")
    manager.add_plant(tomato)
    manager.add_plant(lettuce)
    manager.add_plant(unknown)
    print("Watering plants...")
    manager.water_plants()
    print("Checking plant health...")
    manager.check_plant_health(lettuce)
    print("Garden management system test complete!")
