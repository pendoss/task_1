import random
from functools import reduce
from math import gcd


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


def lcm_of_three(numbers):
    return reduce(lcm, numbers)


def generate_numbers():
    return [random.randint(1, 100) for _ in range(3)]


def nok():
    numbers = [random.randint(1, 100) for _ in range(3)]
    answer = lcm_of_three(numbers)

    return numbers, answer