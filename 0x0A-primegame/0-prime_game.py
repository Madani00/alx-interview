#!/usr/bin/python3
""" prime game """


def isWinner(x, nums):
    """
    this function returns name of the player that won the most rounds
    """
    if not nums or x < 1:
        return None

    n = max(nums)
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    prime_count = [0] * (n + 1)
    for i in range(1, n + 1):
        prime_count[i] = prime_count[i - 1] + int(sieve[i])

    maria_score = 0
    ben_score = 0

    for num in nums:
        if prime_count[num] % 2 == 0:
            ben_score += 1
        else:
            maria_score += 1

    if maria_score > ben_score:
        return "Maria"
    elif ben_score > maria_score:
        return "Ben"
    else:
        return None
