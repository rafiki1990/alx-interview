#!/usr/bin/python3
"""Define 2D matrix module."""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise in-place.

    Args:
    - matrix (list of lists): The 2D matrix to be rotated.

    Returns:
    - None: The matrix is modified in-place.
    """
    n = len(matrix)  # Get the size of the matrix

    # Transpose the matrix (rows become columns)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row to complete the rotation
    for i in range(n):
        matrix[i].reverse()
