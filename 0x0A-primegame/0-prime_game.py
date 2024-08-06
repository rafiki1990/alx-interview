#!/usr/bin/python3
"""
Prime Game
"""


def isWinner(x, nums):
    """
    Determines the winner of the prime game.

    Args:
        x (int): The number of rounds.
        nums (list): An array of n for each round.

    Returns:
        str: The name of the player that won the most rounds.
             If the winner cannot be determined, returns None.
    """
    def is_prime(num):
        """
        Checks if a number is prime.

        Args:
            num (int): The number to check.

        Returns:
            bool: True if the number is prime, False otherwise.
        """
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def winner_of_round(n):
        """
        Determines the winner of a single round.

        Args:
            n (int): The upper limit of the numbers for the round.

        Returns:
            str: The name of the winner (Maria or Ben).
        """
        primes = [i for i in range(2, n + 1) if is_prime(i)]
        if len(primes) % 2 == 0:
            return "Ben"
        else:
            return "Maria"

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = winner_of_round(n)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
