#================================
# Working process:
#   1. We define a backtracking function that takes the starting index and the current path as parameters.
#   2. We check if the sorted version of the current path is not already in the output list. If it's not, we add a copy of the sorted path to the output list.
#   3. We iterate through the nums list from the starting index to the end, adding each number to the current path and recursively calling the backtracking function with the next index.
#   4. After the recursive call, we remove the last number from the path to backtrack and explore other combinations.
# Issue: The current implementation checks for duplicates by sorting the path and checking if it's already in the output list, which can be inefficient, which increases the time complexity.
#================================


class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        output = []

        def backtrack(start, path):
            if sorted(path) not in output:
                output.append(sorted(path[:]))

            for i in range(start, len(nums)):
                path.append(nums[i])

                backtrack(i+1, path)

                path.pop()

        backtrack(0,[])

        return output