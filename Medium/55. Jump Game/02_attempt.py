#================================
# Working process:
#   1. Define a function canJump that takes a list of integers nums as input, representing the maximum jump length at each position in the array.
#   2. Initialize a variable max_range to 0, representing the farthest index that can be reached so far.
#   3. Use a for loop to iterate through the array, with i representing the current index and jump representing the maximum jump length at that index.
#  4. Inside the loop, check if max_range is greater than or equal to the last index of the array
#      - If it is, return True, indicating that it is possible to reach the last index.
#   5. If the current index i is greater than max_range, return False, indicating that it is not possible to move forward and reach the last index. 
#   6. Update max_range to the maximum of its current value and the sum of the current index i and the jump length at that index.
#  Takeaway: This implementation has a linear time complexity of O(n), as it only requires a single pass through the array, making it efficient for larger input arrays.
#================================


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        max_range = 0

        for i, jump in enumerate(nums):
            if max_range >= len(nums)-1:
                return True

            if i > max_range:
                return False
                
            max_range = max(max_range, i + jump)