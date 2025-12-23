def ft_plant_age() -> None:
    """
    Description:
        Function asks for a plant’s age in days and tells if it’s
        ready to harvest (more than 60 days) or not.
    Args:
        None
    Returns:
        None
    """
    plant_age = int(input("Enter plant age in days: "))
    if plant_age > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
