#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list): A list of lists representing the locked boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """

    total_boxes = len(boxes)
    unlocked_boxes = set([0])
    queue = [0]

    while queue:
        current_box = queue.pop(0)
        
        for key in boxes[current_box]:
            if key < total_boxes and key not in unlocked_boxes:
                unlocked_boxes.add(key)
                queue.append(key)
    
    return len(unlocked_boxes) == total_boxes
