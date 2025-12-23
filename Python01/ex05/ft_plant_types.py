class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Description:
            Initializes the base attributes for any plant instance.
        Arguments:
            name (str): The name of the plant.
            height (int): The height of the plant in centimeters.
            age (int): The age of the plant in days.
        """
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """
        Description:
            Initializes a new Flower instance with color attribute.
        Arguments:
            name (str): Name.
            height (int): Height in cm.
            age (int): Age in days.
            color (str): Flower color.
        """
        super().__init__(name, height, age)
        self.color = color

    def get_info(self) -> str:
        """
        Description:
            Returns formatted details specific to the flower.
        """
        return f"{self.name} (Flower): {self.height}cm, {self.age} days, {self.color} color"

    def bloom(self) -> str:
        """
        Description:
            Returns a blooming message.
        """
        return f"{self.name} is blooming beautifully!"


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int) -> None:
        """
        Description:
            Initializes a new Tree instance with trunk diameter.
        Arguments:
            name (str): Name.
            height (int): Height in cm.
            age (int): Age in days.
            trunk_diameter (int): Diameter in cm.
        """
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def get_info(self) -> str:
        """
        Description:
            Returns formatted details specific to the tree.
        """
        return f"{self.name} (Tree): {self.height}cm, {self.age} days, {self.trunk_diameter}cm diameter"

    def produce_shade(self) -> str:
        """
        Description:
            Calculates shade area.
        """
        shade_area = self.trunk_diameter * 1.56
        return f"{self.name} provides {int(shade_area)} square meters of shade"


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int, harvest_season: str, vitamin_type: str) -> None:
        """
        Description:
            Initializes a new Vegetable instance.
        """
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.vitamin_type = vitamin_type

    def get_info(self) -> str:
        """
        Description:
            Returns formatted details specific to the vegetable.
        """
        return f"{self.name} (Vegetable): {self.height}cm, {self.age} days, {self.harvest_season} harvest"

    def nutritional_value(self) -> str:
        """
        Description:
            Returns nutritional info.
        """
        return f"{self.name} is rich in vitamin {self.vitamin_type}"


if __name__ == "__main__":
    rose = Flower("Rose", 25, 30, "red")
    oak = Tree("Oak", 500, 1825, 50)
    tomato = Vegetable("Tomato", 80, 90, "summer", "C")
    tulip = Flower("Tulip", 15, 7, "yellow")
    willow = Tree("Weeping Willow", 800, 730, 45)
    kivi = Vegetable("Kiwi", 250, 150, "autumn", "K")

    print("=== Garden Plant Types ===")
    print("")
    print(f"{rose.get_info()}")
    print(rose.bloom())
    print("")
    print(f"{oak.get_info()}")
    print(oak.produce_shade())
    print("")
    print(f"{tomato.get_info()}")
    print(tomato.nutritional_value())
