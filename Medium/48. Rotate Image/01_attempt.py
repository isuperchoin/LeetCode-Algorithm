#================================
# Working process:
#   1. Transpose the matrix by swapping elements across the diagonal
#   2. Reverse each row to achieve a 90-degree clockwise rotation
#  TakeAway: Understanding how to manipulate a 2D matrix in-place, and how to perform a rotation by combining transposition and row reversal.
#================================


class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for row in range(n):
            for col in range(row+1, n):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        for i in matrix:
            i.reverse()