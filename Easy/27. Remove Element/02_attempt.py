#================================
# Working process:
#   1. Iterate over nums list
#   2. Compare each words with val
#   3. If not equal to val, index it to be ith and increase pointer
#   5. Return pointer
# Refinement: No more unnecessry variables and substitution
# TakeAway: Learning how to use double pointer method
#================================


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:

        pointer = 0

        for i in nums:
            if i != val:
                nums[pointer] = i
                pointer += 1

        return pointer


        