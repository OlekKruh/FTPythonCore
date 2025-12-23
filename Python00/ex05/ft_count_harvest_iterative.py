def ft_count_harvest_iterative() -> None:
    """
    Description:
        Functions count from 1 to a given number,
        printing each day until harvest time.
    Args:
        None
    Returns:
        None
    """
    days_to_harvest = int(input("Days until harvest: "))
    for i in range(1, days_to_harvest + 1, 1):
        print(f"day: {i}")
    print("Harvest time!")
