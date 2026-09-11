#================================
# Working process:
#   1. We define a backtracking function that takes the starting index, the current path, and the current sum as parameters.
#   2. We check if the length of the current path is equal to k and the current sum is equal to n. If both conditions are met, we add a copy of the current path to the output list and return.
#   3. We iterate through the numbers from the starting index to 9, adding each number to the current path and updating the current sum.
#   4. If the current sum exceeds n, we return early to avoid unnecessary computations
#   5. After the recursive call, we remove the last number from the path and subtract it from the current sum to backtrack and explore other combinations.
#   6. Finally, we return the output list containing all valid combinations.
# TakeAway: The backtracking approach is efficient for generating combinations, and the early return when the current sum exceeds n helps to reduce the search space.
#================================


class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        output = []

        def backtrack(start, path, ksum):
            if len(path) == k and ksum == n:
                output.append(path[:])
                return

            for i in range(start, 9):
                if ksum + i+1 > n:
                    return
                
                path.append(i+1)
                ksum += i+1

                backtrack(i+1, path, ksum)

                ksum -= path.pop()

        backtrack(0, [], 0)

        return output