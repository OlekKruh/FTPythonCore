class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Description:
            Initializes a new Plant instance.
            Stores the initial height to calculate total growth later efficiently.
        Arguments:
            name (str): The name of the plant.
            height (int): The current height in cm.
            age (int): The current age in days.
        """
        self.name = name
        self.height = height
        self.age = age
        self.initial_height = height

    def get_info(self) -> None:
        """
        Description:
            Prints the current status of the plant (name, height, age) to the console.
        """
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def grow(self) -> None:
        """
        Description:
            Increases the plant's height by 1 unit to simulate growth.
        """
        self.height += 1

    def age_plant(self) -> None:
        """
        Description:
            Increments the plant's age by 1 day.
        """
        self.age += 1


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)

    # Day 1
    print("=== Day 1 ===")
    rose.get_info()
    # Day 2
    rose.grow()
    rose.age_plant()
    # Day 3
    rose.grow()
    rose.age_plant()
    # Day 4
    rose.grow()
    rose.age_plant()
    # Day 5
    rose.grow()
    rose.age_plant()
    # Day 6
    rose.grow()
    rose.age_plant()
    # Day 7
    rose.grow()
    rose.age_plant()
    print("=== Day 7 ===")
    rose.get_info()
    # Calculating growth dynamically to avoid data redundancy in the class
    growth = rose.height - rose.initial_height
    print(f"Growth this week: +{growth}cm")
