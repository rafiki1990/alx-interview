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

    # Initialize the dp array with a large value representing infinity
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins are needed to make a total of 0

    # Iterate over each coin
    for coin in coins:
        # Update the dp array for all amounts from coin to total
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # Check if the total can be made with the given coins
    return dp[total] if dp[total] != float('inf') else -1

# Example usage:
coins = [1, 2, 25]
total = 37
print(makeChange(coins, total))  # Expected output: 7

coins = [1256, 54, 48, 16, 102]
total = 1453
print(makeChange(coins, total))  # Expected output: -1
