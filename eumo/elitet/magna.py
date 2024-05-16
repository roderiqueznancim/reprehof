def intToDecimal(qty, decimal):
    """Converts an integer to a decimal string with the specified number of decimal places.

    Args:
        qty (int): The integer to convert.
        decimal (int): The number of decimal places to use.

    Returns:
        str: The decimal string representation of the integer.
    """

    if decimal < 0:
        raise ValueError("Decimal places must be non-negative.")

    # Convert the integer to a string.
    qty_str = str(qty)

    # Add the decimal point.
    qty_str += "."

    # Add the specified number of zeros.
    qty_str += "0" * decimal

    # Return the decimal string.
    return qty_str
