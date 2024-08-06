#!/usr/bin/python3

def isWinner(x, nums):
    if not nums or x < 1:
        return None

    max_num = max(nums)
    
    # Step 1: Generate all prime numbers up to the maximum number in nums using Sieve of Eratosthenes
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers
    for start in range(2, int(max_num**0.5) + 1):
        if is_prime[start]:
            for multiple in range(start * start, max_num + 1, start):
                is_prime[multiple] = False
    
    primes = [num for num, prime in enumerate(is_prime) if prime]

    # Step 2: Function to determine the winner for a given n
    def determine_winner(n):
        available = [True] * (n + 1)
        turn = 0  # 0 for Maria, 1 for Ben
        
        for prime in primes:
            if prime > n:
                break
            if available[prime]:
                turn += 1
                for multiple in range(prime, n + 1, prime):
                    available[multiple] = False
        
        # Maria starts first (turn is 0), so if turn is even, Maria had the last move
        return "Maria" if turn % 2 != 0 else "Ben"

    # Step 3: Determine winners for all games and count wins
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        winner = determine_winner(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1
    
    # Step 4: Determine overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Example usage:
if __name__ == "__main__":
    x = 3
    nums = [4, 5, 1]
    print(isWinner(x, nums))  # Output should be "Ben"
