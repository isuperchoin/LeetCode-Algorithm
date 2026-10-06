#================================
# Working process:
#   1. Use a sliding window approach to find the minimum length of a contiguous subarray whose sum is greater than or equal to the target.
#   2. Expand the window by moving the right pointer and add the current element to the window sum.
#   3. When the window sum is greater than or equal to the target, update the minimum length and shrink the window from the left until the window sum is less than the target.
#  TakeAway: Understanding how to use the sliding window technique to solve problems involving contiguous subarrays and how to efficiently find the minimum length of such subarrays that meet a certain condition
#================================


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        window_sum = 0
        window_len = float("inf")

        for right in range(len(nums)):
            window_sum += nums[right]

            while window_sum >= target:
                if window_len > right - left +1:
                    window_len = right - left +1
                window_sum -= nums[left]
                left += 1

        return 0 if window_len == float("inf") else window_len

