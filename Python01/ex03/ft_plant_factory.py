class Plant:
    total_plants = 0

    def __init__(self, name, height, age):
        """
        Description:
            Initializes a new plant and increments the class counter.
            Displays creation info immediately to streamline the process.
        Arguments:
            name (str): The name of the plant.
            height (int): The current height.
            age (int): The current age.
        """
        self.name = name
        self.height = height
        self.age = age

        Plant.total_plants += 1

        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")

    p1 = Plant("Rose", 25, 30)
    p2 = Plant("Oak", 200, 365)
    p3 = Plant("Cactus", 5, 90)
    p4 = Plant("Sunflower", 80, 45)
    p5 = Plant("Fern", 15, 120)

    print("")
    print(f"Total plants created: {Plant.total_plants}")
