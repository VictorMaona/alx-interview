#!/usr/bin/python3
'''the matrix 2D'''


def rotate_2d_matrix(matrix):
    '''2d matrix rotation of 90° clockwise
    Returns: Nothing '''
    left, right = 0, len(matrix) - 1

    while left < right:
        for i in range(right - left):
            top, bottom = left, right
            # to save topleft of value
            topLeft = matrix[top][left + i]
            # to move bottom left on top left
            matrix[top][left + i] = matrix[bottom - i][left]
            # to move bottom right to the bottom left
            matrix[bottom - i][left] = matrix[bottom][right - i]
            # to move top right of bottom right
            matrix[bottom][right - i] = matrix[top + i][right]
            # to move top left to the top right
            matrix[top + i][right] = topLeft
        right -= 1
        left += 1
