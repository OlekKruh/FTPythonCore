def garden_operations(operation: str):
    """
    Description:
        Performs garden operations that intentionally trigger specific Python errors.
    Args:
        operation (list): The name of the error to simulate("ValueError", etc.).
    Returns:
        Any: Returns a result if successful (though mostly designed to fail),
             or None if the operation name is unknown.
    """
    if operation == "ValueError":
        return int("abc")
    elif operation == "ZeroDivisionError":
        return 10/0
    elif operation == "FileNotFoundError":
        return open("missing.txt")
    elif operation == "KeyError":
        plants = {"rose": 5, "tulip": 3}
        return print(plants["cactus"])
    return None


def test_error_types():
    """
    Description:
        Runs a sequence of tests to demonstrate catching different exception types.
        Iterates through a list of expected error names, triggers them,
        and catches them individually. Also demonstrates catching multiple
        exception types in a single block.
    """
    operations = ["ValueError", "ZeroDivisionError", "FileNotFoundError", "KeyError"]

    for operation in operations:
        try:
            print(f"Testing {operation}...")
            garden_operations(operation)
        except ValueError:
            print(f"Caught {operation}: invalid literal for int()\n")
        except ZeroDivisionError:
            print(f"Caught {operation}: division by zero\n")
        except FileNotFoundError:
            print(f"Caught {operation}: No such file 'missing.txt'\n")
        except KeyError:
            print(f"Caught {operation}:'missing\\_plant'\n")

    try:
        print("Testing multiple errors together...")
        garden_operations("ValueError")
        garden_operations("ZeroDivisionError")
    except (ZeroDivisionError, ValueError):
        print("Caught an error, but program continues!\n")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===\n")
    test_error_types()
    print("All error types tested successfully!")
