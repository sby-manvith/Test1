# Test1

A simple Python calculator program created to demonstrate and test GitHub Projects and Code Scanning (CodeQL).

## Features

- Basic arithmetic operations: addition, subtraction, multiplication, division
- Mathematical utilities: power, factorial, prime-number check

## Usage

Run the demo:

```bash
python calculator.py
```

Run the unit tests:

```bash
python -m unittest test_calculator.py -v
```

## Project Structure

| File | Description |
|------|-------------|
| `calculator.py` | Core calculator functions |
| `test_calculator.py` | Unit tests for all calculator functions |

## Functions

| Function | Signature | Description |
|----------|-----------|-------------|
| `add` | `add(a, b)` | Returns `a + b` |
| `subtract` | `subtract(a, b)` | Returns `a - b` |
| `multiply` | `multiply(a, b)` | Returns `a * b` |
| `divide` | `divide(a, b)` | Returns `a / b`; raises `ValueError` if `b == 0` |
| `power` | `power(base, exponent)` | Returns `base ** exponent` |
| `factorial` | `factorial(n)` | Returns `n!`; raises `ValueError` for negative integers |
| `is_prime` | `is_prime(n)` | Returns `True` if `n` is prime, `False` otherwise |