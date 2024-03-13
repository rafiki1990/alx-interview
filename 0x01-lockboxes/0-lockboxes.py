#!/usr/bin/python3
"""
Module for checking if all boxes can be unlocked.
"""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.

    Args:
    - boxes (list of lists):    A list of boxes where each box
                                may contain keys to other boxes.

    Returns:
    - bool: True if all boxes can be opened, False otherwise.
    """
    # Set to keep track of opened boxes
    opened_boxes = set()

    # Initially, the first box is open
    opened_boxes.add(0)

    # List to keep track of keys to be checked
    keys_to_check = boxes[0]

    # Loop until there are no more keys to check
    while keys_to_check:
        # Get the next key
        key = keys_to_check.pop()

        # Check if the key opens a new box
        if key < len(boxes) and key not in opened_boxes:
            # Open the box and add its keys to the list of keys to check
            opened_boxes.add(key)
            keys_to_check.extend(boxes[key])

    # Check if all boxes have been opened
    return len(opened_boxes) == len(boxes)
