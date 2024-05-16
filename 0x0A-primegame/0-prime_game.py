#!/usr/bin/python3
"""
Describe Wineer function which solves the Prime Game puzzle.
"""


def primes(n):
    """prime numbers between 1 and n inclusive returned
       Args:
        n (int): top border of range lower bound is always 1
    """
    prime = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if (sieve[p]):
            prime.append(p)
            for i in range(p, n + 1, p):
                sieve[i] = False
    return prime


def isWinner(x, nums):
    """
    decides the Prime Game winner
    Args:
        x (int): amount of game rounds
        nums (int): maximum range allowed in each round
    Return:
        Winners name Ben or Maria or None if winner is not identified
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for i in range(x):
        prime = primes(nums[i])
        if len(prime) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
