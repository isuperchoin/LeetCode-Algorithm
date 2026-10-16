#================================
# Working process:
#   1. Define a function exist that takes a 2D list board and a string word as input, representing the board of characters and the word to search for.
#   2. Initialize a list directions containing tuples representing the four possible directions (down, up, right, left) to move in the board.
#   3. Define a recursive helper function dfs that takes the current row, column, and index of the character in the word as parameters.
#   4. In the dfs function:
#      - Check if the current row and column are within the bounds of the board.
#      - If the current index is equal to the length of the word minus one and the character at the current position in the board matches the character at the current index in the word, return True, indicating that the word has been found.
#      - If the character at the current position in the board matches the character at the current index in the word, temporarily mark the current position in the board as visited by replacing it with a special character (e.g., "#").
#      - Iterate through the four possible directions and recursively call dfs for each direction, incrementing the index by 1. If any of the recursive calls return True, propagate the True value back up the call stack.
#      - After exploring all directions, restore the original character at the current position in the board and return.
#      - If the character at the current position in the board does not match the character at the current index in the word, return.
#   5. Iterate through each cell in the board. If the character at the current cell matches the first character of the word, call the dfs function with the current row, column, and index 0. If dfs returns True, return True, indicating that the word has been found in the board.
#   6. If the entire board has been searched and the word has not been found, return False.
#  Takeaway: The implementation uses depth-first search (DFS) to explore all possible paths in the board to find the given word. It efficiently handles backtracking by marking visited cells and restoring them after exploring all directions, ensuring that each cell can be reused in different paths.
#================================


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def dfs(row, col, idx):
            if 0 <= row < len(board) and 0 <= col < len(board[0]):
                if idx == len(word) -1 and board[row][col] == word[idx]:
                    return True
                elif board[row][col] == word[idx]:
                    temp = board[row][col]
                    board[row][col] = "#"

                    for dir_r, dir_c in directions:
                        if dfs(row + dir_r, col + dir_c, idx+1):
                            return True

                    board[row][col] = temp
                    return

                else:
                    return
            else:
                return
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True

        return False