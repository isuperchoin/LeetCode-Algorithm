#================================
# Working process:
#   1. Iterate through nums with double loop variable
#   2. Set comp variable defined as difference of target and list nums's element
#   3. Return the list of comp and i if comp is in the dictionary memo
#   4. Else, put that element in the memo as a key
# Refinement: Shorter runtime by using only one loop
# TakeAway: Learning how to apply library data type
#================================


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        memo = {}

        for i, num in enumerate(nums):
            comp = target - num

            if comp in memo:
                return[memo[comp],i]
            else:
                memo[num] = i