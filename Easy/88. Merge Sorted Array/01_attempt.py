#================================
# Working process:
#   1. Create two pointers, p1 and p2, to point to the end of the valid elements in nums1 and nums2 respectively
#   2. Loop through the nums1 array in reverse order, starting from the end
#   3. Compare the elements pointed by p1 and p2, and place the larger one at the current index of nums1
#   4. Move the pointer of the array from which the element was taken
#   5. If p2 becomes less than 0, break the loop as all elements from nums2 have been merged
#   6. If p1 becomes less than 0, copy the remaining elements from nums2 to nums1 and break the loop
# Issue: Could've done it in more tidy structure
#================================


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        p1 = m-1
        p2 = n-1

        for i in reversed(range(m+n)):
            if p2 < 0:
                break
            if p1 < 0:
                nums1[:p2+1] = nums2[:p2+1]
                break

            if nums1[p1] < nums2[p2]:
                nums1[i] = nums2[p2]
                p2 -= 1
            else:
                nums1[i] = nums1[p1]
                p1 -= 1