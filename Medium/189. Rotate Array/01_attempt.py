#================================
# Working process:
#   1. If k is less than the length of the array, split the array into two parts at the rotation point and concatenate them in reverse order.
#   2. If k is greater than or equal to the length of the array, calculate the effective rotation amount by taking k modulo the length of the array.
#   3. Split and concatenate the array in reverse order.
#  Issue: Unnecessary conditional check for k < len(nums) can be avoided by always calculating k modulo len(nums) to handle cases where k is greater than or equal to the length of the array.
#================================


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k<len(nums):
            nums[:] = nums[len(nums)-k:] + nums[:len(nums)-k]
        else:
            k = k%len(nums)
            nums[:] = nums[len(nums)-k:] + nums[:len(nums)-k]