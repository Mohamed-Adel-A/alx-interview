#!/usr/bin/python3
""" 0. Prime Game """


def is_prime(num):
    """Implementation of the Sieve of Eratosthenes algorithm."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def isWinner(x, nums):
    """Determine the winner of the prime game."""
    if not isinstance(x, int) or x <= 0:
        return None
    if not isinstance(nums, list) or len(nums) != x:
        return None
    wins = {'Maria': 0, 'Ben': 0}
    for n in nums:
        if not isinstance(n, int) or n <= 0:
            return None
        primes_count = sum(1 for i in range(1, n + 1) if is_prime(i))
        if primes_count % 2 == 0:
            wins['Ben'] += 1
        else:
            wins['Maria'] += 1

    if wins['Maria'] == wins['Ben']:
        return None
    return max(wins, key=wins.get)
