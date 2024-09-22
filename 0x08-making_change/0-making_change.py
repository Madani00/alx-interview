#!/usr/bin/python3
"""
greedy algorithm
"""


def makeChange(coins, total):
    """
    Change comes from within
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    n_coins = 0
    for coin in coins:
        if total <= 0:
            break
        n_coins += total // coin
        total = total % coin
    if total != 0:
        return -1
    return n_coins
