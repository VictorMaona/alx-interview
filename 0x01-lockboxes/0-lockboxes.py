#!/usr/bin/python3
'''Task for lists representing the boxes'''


def canUnlockAll(boxes):
    '''accepts a single argument box
    Returns:
        True: Every box can be opened.
        False: Not every package can be opened.
    '''
    length = len(boxes)
    keys = set()
    opened_boxes = []
    i = 0

    while i < length:
        oldi = i
        opened_boxes.append(i)
        keys.update(boxes[i])
        for key in keys:
            if key != 0 and key < length and key not in opened_boxes:
                i = key
                break
        if oldi != i:
            continue
        else:
            break

    for i in range(length):
        if i not in opened_boxes and i != 0:
            return False
    return True
