#================================
# Working process:
#   1. Define a function searchInsert that takes a list of integers nums and an integer target as input, representing the sorted array and the target value to search for.
#   2. Iterate through the list nums using a for loop with an index variable i.
#   3. For each element in nums, check if the current element is greater than or equal to the target value.
#      - If it is, return the current index i, indicating the position where the target should be inserted to maintain the sorted order.
#   4. If the loop completes without finding an element greater than or equal to the target, return the length of the list nums, indicating that the target should be inserted at the end of the list.
#  Takeaway: The implementation uses a simple linear search to find the appropriate index for the target value in a sorted array. It efficiently handles the case where the target is greater than all elements in the array by returning the length of the array, indicating that the target should be inserted at the end.
#================================


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] >= target:
                return i

        return len(nums)