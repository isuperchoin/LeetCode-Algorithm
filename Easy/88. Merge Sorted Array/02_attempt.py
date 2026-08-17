#================================
# Working process:
#   1. create two pointers, p1 and p2, to point to the end of the valid elements in nums1 and nums2 respectively
#   2. loop through the nums1 array in reverse order, starting from the end
#   3. compare the elements pointed by p1 and p2, and place the larger one at the current index of nums1
#   4. move the pointer of the array from which the element was taken
#   5. if either p1 or p2 becomes less than 0, prevent them from reaching to index or in might cause index out of range error
# Refinement: Simpler structure and less comparison operations
# TakeAway: Learning how to use two pointers and reverse loop
#================================


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        p1 = m-1
        p2 = n-1
        i = m+n-1

        while p2 >= 0:

            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[i] = nums1[p1]
                p1 -= 1
            else:
                nums1[i] = nums2[p2]
                p2 -= 1

            i -= 1