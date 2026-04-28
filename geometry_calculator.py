"""
A geometry module providing area and perimeter calculations for common shapes.
"""

import math


def circle_area(radius):
    """Return the area of a circle with the given radius.

    Raises:
        ValueError: If radius is negative.
    """
    if radius < 0:
        raise ValueError("Radius must be non-negative.")
    return math.pi * radius ** 2


def circle_perimeter(radius):
    """Return the circumference of a circle with the given radius.

    Raises:
        ValueError: If radius is negative.
    """
    if radius < 0:
        raise ValueError("Radius must be non-negative.")
    return 2 * math.pi * radius


def rectangle_area(width, height):
    """Return the area of a rectangle.

    Raises:
        ValueError: If width or height is negative.
    """
    if width < 0 or height < 0:
        raise ValueError("Width and height must be non-negative.")
    return width * height


def rectangle_perimeter(width, height):
    """Return the perimeter of a rectangle.

    Raises:
        ValueError: If width or height is negative.
    """
    if width < 0 or height < 0:
        raise ValueError("Width and height must be non-negative.")
    return 2 * (width + height)


def triangle_area(base, height):
    """Return the area of a triangle given its base and height.

    Raises:
        ValueError: If base or height is negative.
    """
    if base < 0 or height < 0:
        raise ValueError("Base and height must be non-negative.")
    return 0.5 * base * height


def triangle_perimeter(a, b, c):
    """Return the perimeter of a triangle given its three side lengths.

    Raises:
        ValueError: If any side is non-positive or the sides do not form a valid triangle.
    """
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("All sides must be positive.")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("The given sides do not form a valid triangle.")
    return a + b + c


def trapezoid_area(base1, base2, height):
    """Return the area of a trapezoid given two parallel bases and height.

    Raises:
        ValueError: If any argument is negative.
    """
    if base1 < 0 or base2 < 0 or height < 0:
        raise ValueError("Bases and height must be non-negative.")
    return 0.5 * (base1 + base2) * height


if __name__ == "__main__":
    print("Geometry Calculator Demo")
    print(f"circle_area(5)              = {circle_area(5):.4f}")
    print(f"circle_perimeter(5)         = {circle_perimeter(5):.4f}")
    print(f"rectangle_area(4, 6)        = {rectangle_area(4, 6)}")
    print(f"rectangle_perimeter(4, 6)   = {rectangle_perimeter(4, 6)}")
    print(f"triangle_area(3, 8)         = {triangle_area(3, 8)}")
    print(f"triangle_perimeter(3, 4, 5) = {triangle_perimeter(3, 4, 5)}")
    print(f"trapezoid_area(4, 6, 5)     = {trapezoid_area(4, 6, 5)}")
