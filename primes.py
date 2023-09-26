"""List of prime numbers generator."""
from typing import List

"""ENTER YOUR SOLUTION HERE!"""


def primes(number_of_primes) -> List[int]:
    if number_of_primes <= 0:
        raise ValueError

    list = []
    number = 2

    while len(list) < number_of_primes:
        if not divisible(number, list):
            list.append(number)

        number += 1

    return list

"""
For an inputted number, and a list of divisors, return true
if the number can be divided by any number in the list,
otherwise, return false.

:param number: the number that we are testing
:param divisors: the list of numbers we check can divide the number
"""
def divisible(number: int, divisors: List[int]) -> bool:
    if not divisors:
        return False

    for divisor in divisors:
        if number % divisor == 0:
            return True

    return False