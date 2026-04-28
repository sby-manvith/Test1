# Test1

A simple Python calculator program created to demonstrate and test GitHub Projects and Code Scanning (CodeQL).

## Features

- Basic arithmetic operations: addition, subtraction, multiplication, division
- Mathematical utilities: power, factorial, prime-number check
- Statistical functions: mean, median, mode, variance, standard deviation

## Usage

Run the demo:

```bash
python calculator.py
```

Run the statistics demo:

```bash
python statistics_calculator.py
```

Run the unit tests:

```bash
python -m unittest test_calculator.py -v
python -m unittest test_statistics_calculator.py -v
```

## Project Structure

| File | Description |
|------|-------------|
| `calculator.py` | Core calculator functions |
| `test_calculator.py` | Unit tests for all calculator functions |
| `statistics_calculator.py` | Statistical functions (mean, median, mode, variance, std dev) |
| `test_statistics_calculator.py` | Unit tests for all statistics functions |

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