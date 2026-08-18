#================================
# Working process:
#   1. Calculate the effective rotation amount by taking k modulo the length of the array.
#   2. Split the array into two parts at the effective rotation point.
#   3. Concatenate the two parts in reverse order and assign it back to the original array.
# Refinement: The unnecessary conditional check for k < len(nums) has been removed, and the index expression has been simplified to use negative indexing for better readability.
# TakeAway: Learning how to rotate an array in Python using slicing and negative indexing
#================================


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)

        nums[:] = nums[-k:] + nums[:-k]