def ft_garden_summary() -> None:
    """
    Description:
        Function asks for a garden name and the number of plants,
        then displays a simple summary with a fixed status message.
    Returns:
        None
    Args:
        None
    """
    name = input("Enter garden name: ")
    plants_num = input("Enter number of plants: ")
    print(f"Garden: {name}")
    print(f"Plants: {plants_num}")
    print("Status: Growing well!")
