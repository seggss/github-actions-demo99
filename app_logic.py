def add_numbers(a, b):
    """Pure function for easy unit testing."""
    if a is None or b is None:
        raise ValueError("Both 'a' and 'b' are required.")
    try:
        return float(a) + float(b)
    except (TypeError, ValueError) as e:
        raise TypeError("Inputs must be numbers or numeric strings.") from e
