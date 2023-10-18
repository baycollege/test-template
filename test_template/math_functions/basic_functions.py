
def mult(a: int, b: int) -> int:
    """Function to multiple two numbers.

    Args:
        a (int): The first number to multiply
        b (int): The second number to multiply

    Returns:
        int: The product of the multiplication
    """
    return a * b


def add(a: int, b: int) -> int:
    """Function to add two numbers.

    Args:
        a (int): The first number to add
        b (int): The second number to add

    Returns:
        int: The sum of the two numbers
    """
    return a + b


def div(a: int, b: int) -> int:
    """Function to divide two numbers.

    Args:
        a (int): The first number to divide
        b (int): The second number to divide

    Raises:
        ZeroDivisionError: Raise a zero error when dividing by zero

    Returns:
        int: The quotient of the division
    """
    if b == 0:
        raise ZeroDivisionError("Can not divide by zero.")

    return a/b


def sub(a: int, b: int) -> int:
    """Function to subtract two numbers

    Args:
        a (int): The first number to subtract
        b (int): The second number to subtract

    Returns:
        int: The difference of the subtraction
    """
    return a-b
