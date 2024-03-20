#!/usr/bin/python3
'''Python 3 Minimum Operations Challenge'''


def minOperations(n):
    '''determines how few operations
    are required in this file to produce
    exactly n H characters.
    Returns:
        Integer : Return 0 if n cannot be achieved.
    '''
    pasted_chars = 1  # number of characters in the file
    clipboard = 0  # how many copies of H there are
    counter = 0  # counter for operations

    while pasted_chars < n:
        # if you haven't yet copied anything
        if clipboard == 0:
            # copy all
            clipboard = pasted_chars
            # increase the operations counter
            counter += 1

        # If you haven't yet pasted anything
        if pasted_chars == 1:
            # for pasting
            pasted_chars += clipboard
            # increase the operations counter
            counter += 1
            # proceed to the following loop
            continue

        remaining = n - pasted_chars  # remaining chars to Paste
        # verify whether it's not feasible by seeing if the clipboard
        # has more than necessary to attain the intended number.
        # meaning that the number of characters in the file is also equal.
        # greater than what's on the clipboard.
        # It is not possible to reach n of chars in either case.
        if remaining < clipboard:
            return 0

        # If it cannot be divided
        if remaining % pasted_chars != 0:
            # paste current clipboard
            pasted_chars += clipboard
            # increment operations counter
            counter += 1
        else:
            # copying all
            clipboard = pasted_chars
            # pasting
            pasted_chars += clipboard
            # increase the operations counter
            counter += 2

    # if the intended outcome was achieved
    if pasted_chars == n:
        return counter
    else:
        return 0
