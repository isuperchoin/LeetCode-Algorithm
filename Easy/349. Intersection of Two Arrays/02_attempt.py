#================================
# Working process:
#   1. Get the intersection of two arrays by converting them to sets and using the set intersection operator (&).
#   2. Convert the resulting set back to a list and return it.
#  Refinement: The time complexity is O(n + m) where n is the length of nums1 and m is the length of nums2, which is more efficient than the previous implementation
#  TakeAway: Using sets can significantly improve the performance of finding intersections in arrays.


class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        return list(set(nums1) & set(nums2))