#================================
# Working process:
#   1. Iterate through nums
#   2. Iterate through nums once again from where we left off
#   3. Check if sum of those two elements of nums are equal to target
# Issue: Way too long Runtime
#================================


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return[i,j]