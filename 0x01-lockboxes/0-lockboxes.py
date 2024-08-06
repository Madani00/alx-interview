#!/usr/bin/python3
""" Determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    """boxes let's start"""
    n = len(boxes)
    opened_boxes = set()
    opened_boxes.add(0)
    stack = [0]

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key not in opened_boxes and key < n:
                opened_boxes.add(key)
                stack.append(key)

    return len(opened_boxes) == n
