def ft_water_reminder() -> None:
    """
    Description:
        Function asks for the number of days since last watering.
        If it’s more than 2 days, print "Water the plants!",
        otherwise print "Plants are fine".
    Args:
        None
    Returns:
        None
    """
    days = int(input("Days since last watering: "))
    if days > 2:
        print("Water the plants!")
    else:
        print("Plants are fine!")
