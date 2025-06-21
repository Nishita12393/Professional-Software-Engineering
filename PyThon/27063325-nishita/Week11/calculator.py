import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(base, exponent):
    return math.pow(base, exponent)

def root(number, degree):
    if number < 0 and degree % 2 == 0:
        raise ValueError("Cannot take even root of a negative number")
    return number ** (1 / degree)

def sine(degrees):
    return math.sin(math.radians(degrees))

def cosine(degrees):
    return math.cos(math.radians(degrees))

def tangent(degrees):
    if degrees % 180 == 90:
        raise ValueError("Tangent undefined at 90, 270, 450... degrees")
    return math.tan(math.radians(degrees))
