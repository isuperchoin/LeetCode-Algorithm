


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        top = None

        for i in nums:
            if i == top:
                return True
            else:
                top = i

        return False