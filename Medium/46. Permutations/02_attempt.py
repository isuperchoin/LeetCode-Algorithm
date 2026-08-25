#================================
# Working process:
#   Same with 01_attempt.py, but using a visited list to keep track of which elements have been used in the current path.
# Refinement: Using a visited list improves the efficiency of checking whether an element is already in the path.
# TakeAway: The visited list allows for O(1) time complexity when checking if an element has been used, compared to O(n) time complexity when checking if an element is in the path list.
#           Learned to use backtracking with a visited list to optimize the solution for generating permutations.
#================================


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        output = []
        visited = [False]*len(nums)

        def backTrack(path):
            if len(path) == len(nums):
                output.append(path[:])
                return

            for i in range(len(nums)):
                if not visited[i]:
                    path.append(nums[i])
                    visited[i] = True

                    backTrack(path)

                    path.pop()
                    visited[i] = False

        backTrack([])

        return output