#!/usr/bin/python3
"""Calcute the perimeter of an island."""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.

    Args:
    grid (List[List[int]]): A list of lists representing the grid where:
        - 0 represents water
        - 1 represents land

    Returns:
    int: The perimeter of the island.

    Constraints:
    - grid is rectangular, with its width and height not exceeding 100
    - The grid is completely surrounded by water
    - There is only one island (or nothing)
    - The island doesn’t have “lakes” (water inside that isn’t connected to
    - the water surrounding the island)
    """
    if not grid:
        return 0

    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4  # Each land cell contributes 4 sides peri

                # Check neighbors
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # Subtract 2 for each adjacent land cell
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
