#!/usr/bin/python3

def make_change(coins, total):
    """Return the fewest number of coins needed to make the total."""
    
    # Edge case: if total is 0 or less, return 0
    if total <= 0:
        return 0

    # Initialize a list to store the minimum number of coins for each amount
    dp = [float('inf')] * (total + 1)

    # Base case: 0 coins are needed to make the total of 0
    dp[0] = 0

    # Iterate through all amounts from 1 to total
    for amount in range(1, total + 1):
        # Check each coin to find the minimum number of coins needed
        for coin in coins:
            if amount - coin >= 0:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still infinity, it means we can't make up the total with the given coins
    return dp[total] if dp[total] != float('inf') else -1
