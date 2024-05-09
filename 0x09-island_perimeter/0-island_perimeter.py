#!/usr/bin/python3
'''The 0x09 Island Perimeter'''


def island_perimeter(grid):
    '''yields island perimeter as specified by the grid'''
    counter = 0
    grid_max = len(grid) - 1  # the grid index for the final list
    lst_max = len(grid[0]) - 1  # the last square in the list index

    for lst_idx, lst in enumerate(grid):
        for land_idx, land in enumerate(lst):
            if land == 1:
                # the left and right
                if land_idx == 0:
                    # the left side
                    counter += 1

                    # the right side
                    if lst[land_idx + 1] == 0:
                        counter += 1
                elif land_idx == lst_max:
                    # the left side
                    if lst[land_idx - 1] == 0:
                        counter += 1

                    # the right side
                    counter += 1
                else:
                    # the left side
                    if lst[land_idx - 1] == 0:
                        counter += 1

                    # the right side
                    if lst[land_idx + 1] == 0:
                        counter += 1

                # the down and top
                if lst_idx == 0:
                    # to the top side
                    counter += 1

                    # to the bottom side
                    if grid[lst_idx + 1][land_idx] == 0:
                        counter += 1
                elif lst_idx == grid_max:
                    # to the top side
                    if grid[lst_idx - 1][land_idx] == 0:
                        counter += 1

                    # to the bottom side
                    counter += 1
                else:
                    # to the top side
                    if grid[lst_idx - 1][land_idx] == 0:
                        counter += 1

                    # to the bottom side
                    if grid[lst_idx + 1][land_idx] == 0:
                        counter += 1

    return counter
