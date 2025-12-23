def ft_count_harvest_recursive(days: int = None) -> None:
    """
    Description:
        Functions count from 1 to a given number,
        printing each day until harvest time.
    Args:
        days(int): Optional. Number of days to harvest.
    Returns:
        None
    """
    is_top_level = False
    if days is None:
        days = int(input("Days until harvest: "))
        is_top_level = True
    if days > 1:
        ft_count_harvest_recursive(days-1)
    print(f"Day: {days}")
    if is_top_level:
        print("Harvest time!")
