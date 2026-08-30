#================================
# Working process:
#   1. We define a backtracking function that takes the starting index and the current path as parameters.
#   2. If the length of the current path equals k, we add a copy of the path to the output list and return.
#   3. We iterate through the numbers from the starting index to n, adding each number to the path and recursively calling the backtracking function with the next index.
#   4. After the recursive call, we remove the last number from the path to backtrack and explore other combinations.
# TakeAway: Practicing how to utilize backtracking in generating combinations of numbers.
#================================


class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        output = []
        def backtrack(start, path):
            if len(path)==k:
                output.append(path[:])
                return

            for i in range(start, n+1):
                
                path.append(i)

                backtrack(i+1, path)

                path.pop()

        backtrack(1,[])

        return output