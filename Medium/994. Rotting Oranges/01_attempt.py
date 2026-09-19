#================================
# Working process:
#   1. We initialize a queue to keep track of the rotten oranges and a counter for the number of fresh oranges.
#   2. We iterate through the grid to populate the queue with the positions of the rotten oranges and count the number of fresh oranges.
#   3. We perform a breadth-first search (BFS) using the queue. For each rotten orange, we check its four neighboring cells (up, down, left, right). If a neighboring cell contains a fresh orange, we rot it (change its value to 2), decrement the fresh orange counter, and add its position to the queue.
#   4. We keep track of the number of minutes that have passed during the BFS process. Each level of BFS represents one minute.
#   5. The process continues until there are no more rotten oranges to process or there are no fresh oranges left.
#   6. Finally, we return the number of minutes taken to rot all fresh oranges if there are no fresh oranges left; otherwise, we return -1 to indicate that not all fresh oranges can be rotted.
# TakeAway: The BFS approach is effective for simulating the spread of rot in a grid, and using a queue allows us to process all rotten oranges at the same time, ensuring that we accurately track the time taken for the rot to spread.
#================================



from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        queue = deque()
        m,n = len(grid), len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        minutes = 0
        fresh_remaining = 0

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh_remaining += 1

        while queue and fresh_remaining >0:
            minutes += 1

            for i in range(len(queue)):

                r,c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_remaining -= 1
                        queue.append((nr,nc))
            
        return minutes if fresh_remaining == 0 else -1