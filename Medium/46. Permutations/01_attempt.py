#================================
# Working process:
#   1. Create an output list to store the permutations of nums.
#   2. Define a backtracking function that takes a path list as an argument.
#   3. If the length of the path list is equal to the length of nums, add it to the output list and return.
#   4. Iterate through nums and check if each element is not already in the path list. If not, append it to the path list and call the backtracking function recursively.
#   5. After the recursive call, remove the last element from the path list to backtrack.
#   6. Call the backtracking function with an empty path list to start the process.
#   7. Return the output list containing all permutations of nums.
#  Issue: The current implementation has a time complexity of O(n!) where n is the length of nums.
#================================


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        output = []

        def backTrack(path):
            if len(path) == len(nums):
                output.append(path[:])
                return

            for i in nums:
                if not i in path:
                    path.append(i)

                    backTrack(path)

                    path.pop()

        backTrack([])

        return output