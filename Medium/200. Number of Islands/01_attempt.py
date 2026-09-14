#================================
# Working process:
#   1. We define a depth-first search (DFS) function that takes the current row and column as parameters.
#   2. In the DFS function, we check if the current cell is out of bounds or if it is water ("0"). If so, we return.
#   3. If the current cell is land ("1"), we mark it as visited by changing its value to "0".
#   4. We then recursively call the DFS function for the neighboring cells (up, down, left, right).
#   5. In the main function, we iterate through each cell in the grid. If we find a land cell ("1"), we increment the island count and call the DFS function to mark all connected land cells as visited.
#   6. Finally, we return the total number of islands found in the grid.
# TakeAway: The DFS approach is effective for exploring connected components in a grid, and marking visited cells helps to avoid counting the same island multiple times.
#================================


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(r,c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == "0":
                return
            
            grid[r][c] = "0"

            dfs(r-1, c)
            dfs(r, c-1)
            dfs(r+1, c)
            dfs(r, c+1)  

        island_num = 0

        m = len(grid)
        n = len(grid[0])

        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1":
                    island_num += 1
                    dfs(row, col)
        
        return island_num