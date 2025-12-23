class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Description:
            Initializes a new instance of the Plant class with the specified name, height, and age.
        Arguments:
            name (str): The name of the plant.
            height (int): The height of the plant in centimeters.
            age_day (int): The age of the plant in days.
        """
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)

    print("=== Garden Plant Registry ===")
    print(f"{rose.name}: {rose.height}cm, {rose.age} days old")
    print(f"{sunflower.name}: {sunflower.height}cm, {sunflower.age} days old")
    print(f"{cactus.name}: {cactus.height}cm, {cactus.age} days old")
