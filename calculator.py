# https://github.com/ST245-y/Lab-11-ST-/tree/main
# Partner 1: Sakshi Tripathy
# Partner 2: Completed independently/ no partner

import math


def square_root(a):
    if a < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    return math.sqrt(a)


def hypotenuse(a, b):
    return math.hypot(a, b)


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a


def logarithm(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Logarithm base must be positive and cannot equal 1")
    if b <= 0:
        raise ValueError("Logarithm argument must be positive")
    return math.log(b, a)


def exponent(a, b):
    return a ** b


# Alternative function names from the second set of instructions

def sub(a, b):
    return subtract(a, b)


def mul(a, b):
    return multiply(a, b)


def div(a, b):
    return divide(a, b)


def log(a, b):
    return logarithm(a, b)


def exp(a, b):
    return exponent(a, b)
