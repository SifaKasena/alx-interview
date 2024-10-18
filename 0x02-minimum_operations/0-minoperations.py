#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """
    Calculate the minimum number of operations needed to achieve
    exactly n 'H' characters in a text file, starting with a single 'H'.
    The only operations allowed are copying all the characters
    and pasting them.

    Args:
        n (int): The target number of 'H' characters.

    Returns:
        int: The minimum number of operations required to reach
        exactly n 'H' characters. If n is less than or equal to 1, returns 0.
    """
    if n <= 1:
        return 0

    for i in range(2, n + 1):
        if n % i == 0:
            return minOperations(n // i) + i

    return n
