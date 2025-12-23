def ft_seed_inventory(name: str, quant: int, unit: str) -> None:
    """
    Description:
        Function manages seed packets, displaying information
        about different seed types and quantities.
    Args:
        name (str): seeds type.
        quant (int): seeds quantity.
        unit (str): measurement unit.
    Returns:
        None
    """
    form_name = name.capitalize()
    if unit == "packets":
        print(f"{form_name} seeds: {quant} {unit} available")
    elif unit == "grams":
        print(f"{form_name} seeds: {quant} {unit} total")
    elif unit == "area":
        print(f"{form_name} seeds: covers {quant} square meters")
    else:
        print("Unknown unit type.")
