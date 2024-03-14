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

    # Create a list to store the minimum number of coins needed for each total from 0 to 'total'
    dp = [float('inf')] * (total + 1)

    # Base case: 0 coins needed for a total of 0
    dp[0] = 0

    # Iterate through each coin value
    for coin in coins:
        # For each coin value, iterate through each total from 'coin' to 'total'
        for sub_total in range(coin, total + 1):
            # Update the minimum number of coins needed for the current total
            dp[sub_total] = min(dp[sub_total], dp[sub_total - coin] + 1)

    # If 'total' cannot be met by any combination of coins, return -1
    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]
