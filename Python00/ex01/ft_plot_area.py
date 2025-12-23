def ft_plot_area() -> None:
    """
    Description:
        Function asks for length and width,
        then calculates and displays the area.
    Args:
        None
    Returns:
        None
    """
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))
    print(f"Plot aria: {length * width}")
