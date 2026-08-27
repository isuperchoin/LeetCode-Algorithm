#================================
# Working process:
#   1. Iterate through the nums list using a for loop.
#   2. For each element, check if it is equal to the target value.
#   3. If a match is found, return the index of that element.
#   4. If the loop completes without finding a match, return -1 to indicate that the target value is not present in the list.
#  Issue: The current implementation has a time complexity of O(n) where n is the length of nums. A more efficient approach would be to use binary search, which has a time complexity of O(log n) for sorted lists.
#================================


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i

        return -1
        