# Test1

A simple Python calculator program created to demonstrate and test GitHub Projects and Code Scanning (CodeQL).

## Features

- Basic arithmetic operations: addition, subtraction, multiplication, division
- Mathematical utilities: power, factorial, prime-number check
- Statistical functions: mean, median, mode, variance, standard deviation
- Geometry functions: area and perimeter of circles, rectangles, triangles, and trapezoids

## Usage

Run the demo:

```bash
python calculator.py
```

Run the statistics demo:

```bash
python statistics_calculator.py
```

Run the geometry demo:

```bash
python geometry_calculator.py
```

Run the unit tests:

```bash
python -m unittest test_calculator.py -v
python -m unittest test_statistics_calculator.py -v
python -m unittest test_geometry_calculator.py -v
```

## Project Structure

| File | Description |
|------|-------------|
| `calculator.py` | Core calculator functions |
| `test_calculator.py` | Unit tests for all calculator functions |
| `statistics_calculator.py` | Statistical functions (mean, median, mode, variance, std dev) |
| `test_statistics_calculator.py` | Unit tests for all statistics functions |
| `geometry_calculator.py` | Geometry functions (area and perimeter of common shapes) |
| `test_geometry_calculator.py` | Unit tests for all geometry functions |

## Functions

### calculator.py

| Function | Signature | Description |
|----------|-----------|-------------|
| `add` | `add(a, b)` | Returns `a + b` |
| `subtract` | `subtract(a, b)` | Returns `a - b` |
| `multiply` | `multiply(a, b)` | Returns `a * b` |
| `divide` | `divide(a, b)` | Returns `a / b`; raises `ValueError` if `b == 0` |
| `power` | `power(base, exponent)` | Returns `base ** exponent` |
| `factorial` | `factorial(n)` | Returns `n!`; raises `ValueError` for negative integers |
| `is_prime` | `is_prime(n)` | Returns `True` if `n` is prime, `False` otherwise |

### statistics_calculator.py

| Function | Signature | Description |
|----------|-----------|-------------|
| `mean` | `mean(numbers)` | Returns the arithmetic mean of a list |
| `median` | `median(numbers)` | Returns the median value of a list |
| `mode` | `mode(numbers)` | Returns the most frequent value (smallest if tied) |
| `variance` | `variance(numbers)` | Returns the population variance of a list |
| `std_deviation` | `std_deviation(numbers)` | Returns the population standard deviation of a list |

### geometry_calculator.py

| Function | Signature | Description |
|----------|-----------|-------------|
| `circle_area` | `circle_area(radius)` | Returns the area of a circle |
| `circle_perimeter` | `circle_perimeter(radius)` | Returns the circumference of a circle |
| `rectangle_area` | `rectangle_area(width, height)` | Returns the area of a rectangle |
| `rectangle_perimeter` | `rectangle_perimeter(width, height)` | Returns the perimeter of a rectangle |
| `triangle_area` | `triangle_area(base, height)` | Returns the area of a triangle |
| `triangle_perimeter` | `triangle_perimeter(a, b, c)` | Returns the perimeter of a triangle |
| `trapezoid_area` | `trapezoid_area(base1, base2, height)` | Returns the area of a trapezoid |