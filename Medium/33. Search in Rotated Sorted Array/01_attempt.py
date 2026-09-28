#================================
# Working process:
#   1. Use binary search to find the target in a rotated sorted array
#   2. Check if the left half is sorted or the right half is sorted
#   3. If the left half is sorted, check if the target is in that range, if so, search in the left half, otherwise search in the right half
#   4. If the right half is sorted, check if the target is in that range, if so, search in the right half, otherwise search in the left half
# TakeAway: Understanding how to apply binary search in a rotated sorted array and the importance of checking which half is sorted to determine where to search next
#================================



class Solution:
    def search(self, nums: list[int], target: int) -> int:

        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (left + right)//2

            if target == nums[mid]:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid -1
                else:
                    left = mid +1

            elif nums[mid] < nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid +1

                else:
                    right = mid -1     

        return -1