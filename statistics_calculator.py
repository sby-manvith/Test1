"""
A statistics module providing common statistical functions.
"""


def mean(numbers):
    """Return the arithmetic mean of a list of numbers.

    Raises:
        ValueError: If the list is empty.
        TypeError: If numbers is not a list.
    """
    if not isinstance(numbers, list):
        raise TypeError("numbers must be a list.")
    if len(numbers) == 0:
        raise ValueError("Cannot compute mean of an empty list.")
    return sum(numbers) / len(numbers)


def median(numbers):
    """Return the median value of a list of numbers.

    Raises:
        ValueError: If the list is empty.
        TypeError: If numbers is not a list.
    """
    if not isinstance(numbers, list):
        raise TypeError("numbers must be a list.")
    if len(numbers) == 0:
        raise ValueError("Cannot compute median of an empty list.")
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 1:
        return sorted_numbers[mid]
    return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2


def mode(numbers):
    """Return the mode (most frequently occurring value) of a list of numbers.

    If multiple values share the highest frequency, returns the smallest one.

    Raises:
        ValueError: If the list is empty.
        TypeError: If numbers is not a list.
    """
    if not isinstance(numbers, list):
        raise TypeError("numbers must be a list.")
    if len(numbers) == 0:
        raise ValueError("Cannot compute mode of an empty list.")
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    max_count = max(frequency.values())
    modes = sorted(k for k, v in frequency.items() if v == max_count)
    return modes[0]


def variance(numbers):
    """Return the population variance of a list of numbers.

    Raises:
        ValueError: If the list is empty.
        TypeError: If numbers is not a list.
    """
    if not isinstance(numbers, list):
        raise TypeError("numbers must be a list.")
    if len(numbers) == 0:
        raise ValueError("Cannot compute variance of an empty list.")
    avg = mean(numbers)
    return sum((x - avg) ** 2 for x in numbers) / len(numbers)


def std_deviation(numbers):
    """Return the population standard deviation of a list of numbers.

    Raises:
        ValueError: If the list is empty.
        TypeError: If numbers is not a list.
    """
    return variance(numbers) ** 0.5


if __name__ == "__main__":
    data = [4, 1, 2, 2, 3, 5, 4, 4]
    print("Statistics Demo")
    print(f"Data:           {data}")
    print(f"mean:           {mean(data)}")
    print(f"median:         {median(data)}")
    print(f"mode:           {mode(data)}")
    print(f"variance:       {variance(data):.4f}")
    print(f"std_deviation:  {std_deviation(data):.4f}")
