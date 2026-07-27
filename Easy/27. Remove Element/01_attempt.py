#================================
# Working process:
#   1. Iterate over nums list
#   2. Compare each words with val
#   3. If not equal to val, index it to be ith and increase count
#   4. If equal to val, subsitute it with '_'
#   5. Return count
#  Issue: Unnecessary variable and substitution
#================================


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:

        pointer = 0
        count = 0

        for i in nums:
            if i != val:
                nums[pointer] = i
                pointer += 1
                count += 1
            else: nums[nums.index(i)] = '_'

        return count


        
