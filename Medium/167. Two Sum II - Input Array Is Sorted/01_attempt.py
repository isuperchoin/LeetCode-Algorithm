#================================
# Working process:
#   1. Use a two pointer approach to find two numbers in a sorted array that add up to a specific target.
#   2. Initialize two pointers, one at the beginning (left) and one at the end (right) of the array.
#   3. Calculate the sum of the numbers at the left and right pointers. If the sum is equal to the target, return the indices (1-based).
#   4. If the sum is less than the target, move the left pointer to the right to increase the sum.
#   5. If the sum is greater than the target, move the right pointer to the left to decrease the sum.
#  TakeAway: Understanding how to use the two pointer technique to efficiently find pairs in a sorted array that meet a specific condition, and how to return the indices in a 1-based format.
#================================


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        right = len(numbers) -1
        left = 0

        while numbers[left] + numbers[right] != target:
            if numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1

        return [left +1, right +1]