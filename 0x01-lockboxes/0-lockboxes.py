#!/usr/bin/python3
"""Lockboxes"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be unlocked.

    A list of lists is given where each inner list represents a box
    and contains keys to other boxes.
    The function starts with the first box (index 0) and tries to unlock all
    other boxes using the keys found.

    Args:
        boxes (list of list of int): A list of lists where each inner list
        contains integers representing keys to other boxes.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    if len(boxes) == 0:
        return False
    keys = [0]
    for key in keys:
        for new_key in boxes[key]:
            if new_key not in keys and new_key < len(boxes):
                keys.append(new_key)
    if len(keys) == len(boxes):
        return True
    return False
