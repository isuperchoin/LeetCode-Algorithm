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


        
