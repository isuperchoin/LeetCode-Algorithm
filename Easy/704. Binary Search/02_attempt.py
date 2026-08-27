#================================
# Working process:
#   1. Set two pointers, start and end, to the beginning and end of the nums list, respectively.
#   2. While start is less than or equal to end, calculate the mid index as the average of start and end.
#   3. Check if the element at the mid index is equal to the target value. If it is, return the mid index.
#   4. If the element at the mid index is less than the target value, move the start pointer to mid + 1 to search the right half of the list.
#   5. If the element at the mid index is greater than the target value, move the end pointer to mid - 1 to search the left half of the list.
#   6. If the loop completes without finding a match, return -1 to indicate that the target value is not present in the list.
#  Refinement: The current implementation has a time complexity of O(log n) which is efficient for sorted lists.
#  TakeAway: Learning how to implement binary search.
#================================


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        start, end = 0, len(nums)-1
        while start <= end:
            mid = (start+end)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid +1
            else:
                end = mid-1
        
        return -1


        