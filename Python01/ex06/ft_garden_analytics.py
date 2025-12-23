class Plant:
    def __init__(self, plant_name: str, height: int) -> None:
        """
        Description:
            Initializes a base plant with a name and starting height.
        Arguments:
            plant_name (str): The name of the plant.
            height (int): The initial height of the plant in centimeters.
        """
        self.plant_name = plant_name
        self.height = height

    def get_info(self) -> str:
        """
        Description:
            Returns a formatted string representing the basic state of the plant.
        Returns:
            str: A string containing the plant's name and current height.
        """
        return f"- {self.plant_name}: {self.height}cm"

    def grow(self, grow_rate=1) -> int:
        """
        Description:
            Increases the plant's height by a specified rate and prints a confirmation message.
        Arguments:
            grow_rate (int, optional): The amount to increase height by. Defaults to 1.
        Returns:
            int: The amount the plant grew during this cycle.
        """
        self.height += grow_rate
        print(f"{self.plant_name} grew {grow_rate}cm")
        return grow_rate

    def get_prize_points(self) -> int:
        """
        Description:
            Retrieves the prize points associated with the plant. Base plants return 0.
        Returns:
            int: The number of prize points (always 0 for standard plants).
        """
        return 0

    def get_plant_type(self) -> str:
        """
        Description:
            Identifies the type of the plant for polymorphic behavior.
        Returns:
            str: The string identifier 'regular'.
        """
        return "regular"


class FloweringPlant(Plant):
    def __init__(self, plant_name: str, height: int, bloom: str) -> None:
        """
        Description:
            Initializes a flowering plant, extending the base plant attributes with a bloom type.
        Arguments:
            plant_name (str): The name of the plant.
            height (int): The initial height.
            bloom (str): The color or type of the flower.
        """
        super().__init__(plant_name, height)
        self.bloom = bloom

    def get_info(self) -> str:
        """
        Description:
            Extends the base plant info to include details about the flowers.
        Returns:
            str: A formatted string with name, height, and bloom details.
        """
        base_info = super().get_info()
        return f"{base_info}, {self.bloom} flowers (blooming)"

    def get_plant_type(self) -> str:
        """
        Description:
            Identifies the type of the plant for polymorphic behavior.
        Returns:
            str: The string identifier 'flowering'.
        """
        return "flowering"


class PrizeFlower(FloweringPlant):
    def __init__(self, plant_name: str, height: int, bloom: str, prize_points: int) -> None:
        """
        Description:
            Initializes a prize-winning flower with an additional score value.
        Arguments:
            plant_name (str): The name of the plant.
            height (int): The initial height.
            bloom (str): The bloom description.
            prize_points (int): The point value assigned to this prize flower.
        """
        super().__init__(plant_name, height, bloom)
        self.prize_points = prize_points

    def get_info(self) -> str:
        """
        Description:
            Extends the flowering plant info to include the prize point value.
        Returns:
            str: A formatted string with name, height, bloom, and points.
        """
        flowering_plant_info = super().get_info()
        return f"{flowering_plant_info}, Prize points: {self.prize_points}"

    def get_prize_points(self) -> int:
        """
        Description:
            Overrides the base method to return the specific prize points for this flower.
        Returns:
            int: The integer value of the prize points.
        """
        return self.prize_points

    def get_plant_type(self) -> str:
        """
        Description:
            Identifies the type of the plant for polymorphic behavior.
        Returns:
            str: The string identifier 'prize'.
        """
        return "prize"


class GardenManager:
    total_gardens = 0

    def __init__(self) -> None:
        """
        Description:
            Initializes the manager with empty structures for gardens and growth statistics.
        """
        self.gardens = {}
        self.last_growth_stats = {}

    @classmethod
    def get_total_managed_gardens(cls) -> int:
        """
        Description:
            A class method that returns the total number of gardens created across all managers.
            Accesses the class-level variable 'total_gardens'.
        Arguments:
            cls: The class itself.
        Returns:
            int: The total count of managed gardens.
        """
        return cls.total_gardens

    class GardenStats:
        @staticmethod
        def calc_total_growth(plants: list) -> int:
            """
            Description:
                Calculates the total height of all plants in a list using a manual loop (without sum()).
            Arguments:
                plants (list): A list of Plant objects.
            Returns:
                int: The total height accumulation.
            """
            total = 0
            if plants:
                for p in plants:
                    total += p.height
            return total

        @staticmethod
        def calc_prize_points(plants: list) -> int:
            """
            Description:
                Calculates the total prize points of all plants in a list using a manual loop.
            Arguments:
                plants (list): A list of Plant objects.
            Returns:
                int: The total prize points accumulation.
            """
            total = 0
            if plants:
                for p in plants:
                    total += p.get_prize_points()
            return total

    def add_garden(self, garden_name: str) -> None:
        """
        Description:
            Registers a new named garden and increments the global class counter.
        Arguments:
            garden_name (str): The unique name for the new garden.
        """
        if garden_name not in self.gardens:
            self.gardens[garden_name] = []
            GardenManager.total_gardens += 1
        else:
            print("A garden with this name already exists.")

    def add_plant_to_garden(self, garden_name: str, plant: Plant) -> None:
        """
        Description:
            Adds a plant instance to a specific garden's collection.
        Arguments:
            garden_name (str): The name of the target garden.
            plant (Plant): The plant object to add.
        """
        if garden_name in self.gardens:
            self.gardens[garden_name].append(plant)
            print(f"Added {plant.plant_name} to {garden_name} garden")

    def grow_garden(self, garden_name: str):
        """
        Description:
            Triggers the growth process for every plant in a specific garden
            and records total growth statistics.
        Arguments:
            garden_name (str): The name of the garden to grow.
        """
        print(f"\n{garden_name} is helping all plants grow...")
        current_growth_sum = 0

        plants = self.gardens.get(garden_name)
        if plants:
            for plant in plants:
                current_growth_sum += plant.grow()

        self.last_growth_stats[garden_name] = current_growth_sum

    def get_scores_summary(self) -> str:
        """
        Description:
            Constructs a summary string of scores for all gardens.
            Manually joins strings with commas using a loop to avoid using .join().
        Returns:
            str: A comma-separated string summary (e.g., "Alice: 100, Bob: 50").
        """
        keys = sorted(self.gardens.keys())

        result_str = ""
        is_first = True

        for name in keys:
            plants = self.gardens[name]
            total_h = self.GardenStats.calc_total_growth(plants)
            total_p = self.GardenStats.calc_prize_points(plants)
            score = total_h + total_p

            clean_name = name.replace("'s", "")

            if not is_first:
                result_str += ", "

            result_str += f"{clean_name}: {score}"
            is_first = False

        return result_str

    def generate_report(self, garden_name: str):
        """
        Description:
            Generates a comprehensive report including plant details, types, growth stats, and scores.
            Calculates counts and types manually within loops to avoid prohibited functions.
        Arguments:
            garden_name (str): The name of the garden to report on.
        """
        print(f"\n=== {garden_name} Garden Report ===")
        plants = self.gardens.get(garden_name, [])
        print("Plants in garden:")

        plant_count = 0
        regular = 0
        flowering = 0
        prize = 0

        for plant in plants:
            print(plant.get_info())

            plant_count += 1

            p_type = plant.get_plant_type()
            if p_type == "prize":
                prize += 1
            elif p_type == "flowering":
                flowering += 1
            else:
                regular += 1

        total_growth = self.last_growth_stats.get(garden_name, 0)
        total_height = self.GardenStats.calc_total_growth(plants)

        print(f"\nPlants added: {plant_count}, Total growth: {total_growth}cm")
        print(f"Plant types: {regular} regular, {flowering} flowering, {prize} prize flowers")

        print(f"\nHeight validation test: {total_height > 0}")

        all_scores_str = self.get_scores_summary()
        print(f"Garden scores - {all_scores_str}")

        print(f"Total gardens managed: {GardenManager.get_total_managed_gardens()}")


if __name__ == "__main__":
    manager = GardenManager()
    manager.add_garden("Alice's")
    manager.add_garden("Bob's")

    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)

    tulip = FloweringPlant("Tulip", 15, "yellow")
    willow = Plant("Weeping Willow", 800)
    kiwi = PrizeFlower("Kiwi", 25, "white", 15)

    print("=== Garden Management System Demo ===\n")

    manager.add_plant_to_garden("Alice's", oak)
    manager.add_plant_to_garden("Alice's", rose)
    manager.add_plant_to_garden("Alice's", sunflower)

    manager.add_plant_to_garden("Bob's", tulip)
    manager.add_plant_to_garden("Bob's", willow)
    manager.add_plant_to_garden("Bob's", kiwi)

    manager.grow_garden("Alice's")
    manager.grow_garden("Bob's")

    manager.generate_report("Alice's")
