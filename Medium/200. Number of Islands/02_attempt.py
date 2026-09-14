#================================
# Working process:
#   1. We define a depth-first search (DFS) function that takes the current row and column as parameters.
#   2. In the DFS function, we check if the current cell is out of bounds or if it is water ("0"). If so, we return.
#   3. If the current cell is land ("1"), we mark it as visited by changing its value to "0".
#   4. We then recursively call the DFS function for the neighboring cells (up, down, left, right).
#   5. In the main function, we iterate through each cell in the grid. If we find a land cell ("1"), we increment the island count and call the DFS function to mark all connected land cells as visited.
#   6. Finally, we return the total number of islands found in the grid.
# Refactor: Instead of making four separate recursive calls for each direction, we can use a list of direction tuples to iterate through the neighboring cells. This makes the code cleaner and easier to maintain.
# TakeAway: The DFS approach is effective for exploring connected components in a grid, and marking visited cells helps to avoid counting the same island multiple times. Using a direction list simplifies the recursive calls.
#================================


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:

        def dfs(r,c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == "0":
                return
            
            grid[r][c] = "0"

            direction = [(-1,0),(1,0),(0,1),(0,-1)]
            for dr, dc in direction:
                dfs(r + dr, c + dc)

        island_num = 0

        m = len(grid)
        n = len(grid[0])

        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1":
                    island_num += 1
                    dfs(row, col)
        
        return island_num