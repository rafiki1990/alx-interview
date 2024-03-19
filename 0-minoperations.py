#!/usr/bin/python3
"""Module for determining the minimum operations. """


def minOperations(n):
    """
    Calculate the fewest number of operations needed to result in
    exactly n 'H' characters in the file.

    Parameters:
    - n (int): The target number of 'H' characters.

    Returns:
    - int: The fewest number of operations needed. If n is
            impossible to achieve, return 0.
    """

    # Base case: if n is already 1, no operations needed
    if n == 1:
        return 0

    # Initialize an array to store the minimum operations for each
    # number from 1 to n
    dp = [float('inf')] * (n + 1)
    dp[1] = 0  # 1 'H' character, no operations needed

    # Dynamic programming approach to fill the dp array
    for i in range(2, n + 1):
        for j in range(1, i):
            # Check if j is a divisor of i
            if i % j == 0:
                # Update dp[i] with the min operations 4 the current divisor
                dp[i] = min(dp[i], dp[j] + i // j)

    # Return the result, or 0 if it's impossible to achieve
    # exactly n 'H' characters
    return dp[n] if dp[n] != float('inf') else 0
