"""
A simple calculator module for demonstrating GitHub code scanning.
"""


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return the difference of a and b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return the quotient of a divided by b.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def power(base, exponent):
    """Return base raised to the power of exponent."""
    return base ** exponent


def factorial(n):
    """Return the factorial of a non-negative integer n.

    Raises:
        ValueError: If n is negative.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 0:
        raise ValueError("n must be a non-negative integer.")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def is_prime(n):
    """Return True if n is a prime number, False otherwise.

    Returns False for integers less than 2.

    Raises:
        TypeError: If n is not an integer.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def square_root(n):
    """Return the square root of n.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Cannot take the square root of a negative number.")
    return n ** 0.5


if __name__ == "__main__":
    print("Calculator Demo")
    print(f"add(3, 5)       = {add(3, 5)}")
    print(f"subtract(10, 4) = {subtract(10, 4)}")
    print(f"multiply(6, 7)  = {multiply(6, 7)}")
    print(f"divide(15, 3)   = {divide(15, 3)}")
    print(f"power(2, 10)    = {power(2, 10)}")
    print(f"factorial(5)    = {factorial(5)}")
    print(f"is_prime(17)    = {is_prime(17)}")
    print(f"square_root(25) = {square_root(25)}")
