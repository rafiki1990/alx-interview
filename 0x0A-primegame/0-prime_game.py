#!/usr/bin/python3
"""Prime_game module."""


def is_prime(n):
    """
    Check if a number is prime.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def play_round(n):
    """
    Simulate a round of the game.

    Args:
        n (int): The upper limit of the consecutive integers.

    Returns:
        str: The name of the player who wins the round.
    """
    prime_count = sum(1 for i in range(2, n + 1) if is_prime(i))
    return "Maria" if prime_count % 2 == 1 else "Ben"


def isWinner(x, nums):
    """
    Determine the winner of multiple rounds of the game.

    Args:
        x (int): The number of rounds.
        nums (list): A list of integers representing the upper
                    limits for each round.

    Returns:
        str or None: The name of the player who won the most rounds,
        or None if the winner cannot be determined.
    """
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        winner = play_round(n)
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
