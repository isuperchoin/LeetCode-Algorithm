#================================
# Working process:
#   1. Sort the input array nums to bring duplicate elements together.
#   2. Initialize a variable top to None to keep track of the last seen element.
#   3. Iterate through the sorted array nums:
#      - If the current element is equal to top, return True (duplicate found).
#      - Otherwise, update top to the current element.
#   4. If the loop completes without finding duplicates, return False.
#  Issue: The current implementation has a time complexity of O(n log n) due to sorting, which may not be optimal for large input sizes.
#================================


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        top = None

        for i in nums:
            if i == top:
                return True
            else:
                top = i

        return False