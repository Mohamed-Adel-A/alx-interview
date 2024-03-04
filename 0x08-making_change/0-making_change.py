#!/usr/bin/python3
"""
Given a pile of coins of different values,
determine the fewest number of coins needed to meet a given amount total
"""


def makeChange(coins, total):
    """
    Return: fewest number of coins needed to meet total
    If total is 0 or less, return 0
    If total cannot be met by any number of coins you have, return (-1)
    """

    n = len(coins)
    sub = list()

    for i in range (total + 1):
        sub.append(total + 1)
    sub[0] = 0

    for i in range(1, total + 1):
        # For each coin we are given
        for j in range(0, n):
            if coins[j] <= i:
                sub[i] = min(sub[i], sub[i - coins[j]] + 1)

    if sub[total] > total:
        return (-1)

    return sub[total]
