#================================
# Working process:
#   1. Declare a pointer variable to keep track of the index of the next unique element
#   2. Iterate over the list starting from the second element
#   3. If the current element is different from the previous one, place it at the pointer index and increment the pointer
#   4. Return the pointer
# TakeAway: Practicing to use double pointer method
#================================


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        pointer = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[pointer] = nums[i]
                pointer += 1

        return pointer
