#================================
# Working process:
#  1. We define a backtracking function that takes the starting index and the current path as parameters.
#  2. We sort the input list to handle duplicates effectively.
#  3. We iterate through the sorted list, skipping duplicates at each level of recursion.
#  4. We add the current path to the output list at each step.
#  5. We recursively call the backtracking function with the next index and the updated path.
#  6. After the recursive call, we remove the last number from the path to backtrack and explore other combinations.
# Refinement: This implementation efficiently generates all unique subsets of the input list by sorting the list and skipping duplicates without calling 'in' or sorting during the backtracking process, which reduces the time complexity.
# TakeAway: Learning how to implement backtracking to generate unique subsets while handling duplicates in the input list.
#================================



class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        output = []
        nums.sort()

        def backtrack(start, path):
            output.append(path[:])

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])

                backtrack(i+1, path)

                path.pop()

        backtrack(0,[])

        return output