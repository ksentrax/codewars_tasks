"""
Define a function that takes an integer argument and returns True or False depending on if the integer is a prime.
Per Wikipedia, a prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

Examples:

is_prime(1)  /* false */
is_prime(2)  /* true  */
is_prime(-1) /* false */
"""
from math import sqrt


def is_prime(num):
    if num > 1:
        for i in range(2, int(sqrt(num)) + 1):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False
