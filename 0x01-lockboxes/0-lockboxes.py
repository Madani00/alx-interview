#!/usr/bin/python3
""" Determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    """boxes let's start"""
    n = len(boxes)
    visited = set()
    stack = [0]

    while stack:
        box = stack.pop()
        if box not in visited:
            visited.add(box)
            for key in boxes[box]:
                if key not in visited:
                    stack.append(key)

    return len(visited) == n
