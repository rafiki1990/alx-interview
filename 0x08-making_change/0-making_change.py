#!/usr/bin/python3
"""0-making_change module."""

def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total amount.

    Args:
        coins (list of int): List of coin values available.
        total (int): The target total amount.

    Returns:
        int: Fewest number of coins needed to meet the total amount.
             Returns -1 if the total cannot be met by any combination of coins.

    Note:
        - If total is 0 or less, returns 0.
        - The value of a coin will always be an integer greater than 0.
        - You can assume you have an infinite number of each
            denomination of coin in the list.
    """
    if total <= 0:
        return 0

    # Initialize dp array to represent minimum coins needed for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate over each coin
    for coin in coins:
        # Update dp array for each amount from coin to total
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If total is unreachable, return -1; otherwise, return minimum coins needed
    return dp[total] if dp[total] != float('inf') else -1
