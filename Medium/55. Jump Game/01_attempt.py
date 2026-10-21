#================================
# Working process:
#   1. Define a function canJump that takes a list of integers nums as input, representing the maximum jump length at each position in the array.
#   2. Initialize a variable position to 0, representing the current position in the array.
#   3. Use a while loop to iterate through the array until a return statement is reached.
#   4. Inside the loop, calculate the maximum range that can be reached from the current position by adding the current position and the value at that position in nums.
#   5. Check if the maximum range is greater than or equal to the last index of the array
#      - If it is, return True, indicating that it is possible to reach the last index.
#   6. If the value at the current position is 0, return False, indicating that it is not possible to move forward and reach the last index.
#   7. If neither of the above conditions is met, create a list of options representing the jump lengths from the next position to the maximum range.
#   8. Update the position to the index of the option that allows for the farthest jump, using the max function with a custom key that calculates the potential reach from each option.
#  Issue: The current implementation has too heavy time complexity, as it evaluates all possible jump options at each step, leading to inefficiency for larger input arrays.
#================================

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        position = 0
        while True:
            max_range = position + nums[position]
            
            if len(nums)-1 <= max_range:
                return True

            if nums[position] == 0:
                return False

            options = nums[position+1 : max_range +1]
            position += max(range(len(options)), key=lambda i: i + options[i]+1) +1
