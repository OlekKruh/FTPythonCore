def ft_harvest_total() -> None:
    """
    Description:
        Function asks for the weight of each harvest and calculates the total.
    Args:
        None
    Returns:
        None
    """
    day_1_harv = int(input("Day 1 harvest: "))
    day_2_harv = int(input("Day 2 harvest: "))
    day_3_harv = int(input("Day 3 harvest: "))
    print(f"Total harvest: {day_1_harv + day_2_harv + day_3_harv}")
