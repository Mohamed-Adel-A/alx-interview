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

    if total <= 0:
        return 0

    # Create a dictionary to store computed results for different total amounts
    memo = {}

    def dp(target):
        if target in memo:
            return memo[target]
        if target == 0:
            return 0
        if target < 0:
            return float('inf')

        min_coins = float('inf')
        for coin in coins:
            sub_result = dp(target - coin)
            min_coins = min(min_coins, sub_result + 1)

        memo[target] = min_coins
        return min_coins

    result = dp(total)

    if result == float('inf'):
        return -1
    else:
        return result
