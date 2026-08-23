#================================
# Working process:
#   1. Create a memo list to store unique elements from nums1.
#   2. Iterate through nums1 and add unique elements to the memo list.
#   3. Create an output list to store the intersection of nums1 and nums2
#   4. Iterate through nums2 and check if each element is in the memo list
#      and not already in the output list. If both conditions are met, add the element to the output list.
#   5. Return the output list containing the intersection of nums1 and nums2.
#  Issue: The current implementation has a time complexity of O(n*m) where n is the length of nums1 and m is the length of nums2. This can be improved by using sets to reduce the time complexity to O(n + m).
#================================


class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        memo = []
        output = []
        for i in nums1:
            if not i in memo:
                memo.append(i)
        
        for j in nums2:
            if j in memo and not j in output:
                output.append(j)
        
        return output
        