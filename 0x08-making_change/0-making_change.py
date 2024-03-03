#!/usr/bin/python3
"""
Given a pile of coins of different values,
determine the fewest number of coins needed to meet a given amount total
"""


def makeChange(coins, total):
    """
    Return: fewest number of coins needed to meet total
    If total is 0 or less, return 0
    If total cannot be met by any number of coins you have, return -1
    """

    n = len(coins)
    result = []
    i = n - 1
    while(i >= 0):
        while (total >= coins[i]):
            total -= coins[i]
            result.append(coins[i])
            i -= 1
    return (len(total))
