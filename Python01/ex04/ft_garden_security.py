class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Description:
            Initializes a new secure plant instance with private attributes.
            Attributes are marked as private using double underscore (__).
        Arguments:
            name (str): The name of the plant.
            height (int): The initial height.
            age (int): The initial age.
        """
        self.name = name
        self.__height = height if height >= 0 else 0
        self.__age = age if age >= 0 else 0

    # === Safe Getters ===
    def get_height(self) -> int:
        """
        Description:
            Returns the protected height value.
        """
        return self.__height

    def get_age(self) -> int:
        """
        Description:
            Returns the protected age value.
        """
        return self.__age

    def get_info(self) -> str:
        """
        Description:
            Returns formatted string for final output.
        """
        return f"Current plant: {self.name} ({self.__height}cm, {self.__age} days)"

    # === Safe Setters ===
    def set_height(self, new_height: int) -> None:
        """
        Description:
            Updates height with validation.
        """
        if new_height < 0:
            print(f"Invalid operation attempted: height {new_height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = new_height
            print(f"Height updated: {self.__height}cm [OK]")

    def set_age(self, new_age: int) -> None:
        """
        Description:
            Updates age with validation.
        """
        if new_age < 0:
            print(f"Invalid operation attempted: age {new_age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = new_age
            print(f"Age updated: {self.__age} days [OK]")


if __name__ == "__main__":
    print("=== Garden Security System ===")

    plant = SecurePlant("Rose", 0, 0)
    print(f"Plant created: {plant.name}")

    plant.set_height(25)
    plant.set_age(30)

    print("")
    plant.set_height(-5)
    print("")
    print(plant.get_info())
