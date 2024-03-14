#!/usr/bin/python3

def sieve_of_eratosthenes(n):
    """Implementation of the Sieve of Eratosthenes algorithm."""
    primes = [True] * (n+1)
    primes[0] = primes[1] = False
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n+1, p):
                primes[i] = False
        p += 1
    return [i for i in range(n+1) if primes[i]]


def isWinner(x, nums):
    """Determine the winner of the prime game."""
    winners = {'Maria': 0, 'Ben': 0}
    for n in nums:
        primes = sieve_of_eratosthenes(n)
        if len(primes) % 2 == 0:
            winners['Ben'] += 1
        else:
            winners['Maria'] += 1

    if winners['Maria'] == winners['Ben']:
        return None
    return max(winners, key=winners.get)
