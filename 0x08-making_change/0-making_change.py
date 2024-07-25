#!/usr/bin/python3

def makeChange(coins, total):
    if total <= 0:
        return 0
    
    # Initialize the DP table with a large number (infinity)
    dp = [float('inf')] * (total + 1)
    
    # Base case
    dp[0] = 0
    
    # Fill the DP table
    for coin in coins:
        for amount in range(coin, total + 1):
            if dp[amount - coin] != float('inf'):
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    
    # If dp[total] is still infinity, return -1 as it is not possible to form that amount
    return dp[total] if dp[total] != float('inf') else -1

# Example usage
coins = [1, 2, 5]
total = 11
print(makeChange(coins, total))  # Output: 3 (11 = 5 + 5 + 1)
