#!/usr/bin/python3

def makeChange(coins, total):
    if total <= 0:
        return 0
    
    # Initialize the dp array with a large value
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    
    # Update dp array for each coin
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # If dp[total] is still infinity, it means total cannot be met by any combination of coins
    return dp[total] if dp[total] != float('inf') else -1

# Example usage:
coins = [1, 2, 5]
total = 11
print(makeChange(coins, total))  # Output: 3 (5+5+1)
