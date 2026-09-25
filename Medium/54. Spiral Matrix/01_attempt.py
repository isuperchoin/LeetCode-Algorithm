#================================
# Working process:
#   1. Set up four pointers to represent the boundaries of the matrix (top, bottom, left, right)
#   2. Use a while loop to traverse the matrix in a spiral order until the boundaries meet
#   3. In each iteration of the while loop, traverse the top row from left to right, then the right column from top to bottom, then the bottom row from right to left, and finally the left column from bottom to top
#   4. After traversing each side, update the corresponding boundary pointer to move inward
#   5. Append the elements to the output list in the order they are traversed
# TakeAway: Understanding how to manipulate multiple pointers to traverse a 2D matrix in a specific order
#================================


class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        top = 0
        bottom = len(matrix)
        left = 0
        right = len(matrix[0])
        output = []
        
        while bottom > top and left < right:
            for i in range(left, right):
                output.append(matrix[top][i])
            top += 1

            for i in range(top, bottom):
                output.append(matrix[i][right-1])
            right -= 1
            
            if bottom > top and left < right:
                for i in range(right-1, left-1, -1):
                    output.append(matrix[bottom-1][i])
                bottom -= 1    
            else:
                break        

            if bottom > top and left < right:
                for i in range(bottom-1, top-1, -1):
                    output.append(matrix[i][left])
                left += 1
            else:
                break
        
        return output