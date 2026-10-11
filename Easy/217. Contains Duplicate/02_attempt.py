#================================
# Working process:
#   1. Use a set to store unique elements from the input array nums.
#   2. Compare the length of the original array nums with the length of the set no_duplicate.
#   3. If the lengths are equal, it means there are no duplicates, so return False. Otherwise, return True (duplicates exist).
#  Refinement: This implementation has a time complexity of O(n) on average, as adding elements to a set and checking its length are both O(1) operations on average. This is more efficient than the previous sorting-based approach, especially for large input sizes.
#  TakeAway: Understanding how to use a set to efficiently check for duplicates in an array, and how to compare lengths to determine the presence of duplicates.
#================================


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        no_duplicate = set(nums)
        if len(nums) == len(no_duplicate):
            return False
        else:
            return True