#================================
# Working process:
#   1. Use binary search to find the minimum eating speed
#   2. For each speed, calculate the total hours needed
#   3. Adjust the search range based on whether the hours exceed h
#   4. Return the minimum speed that allows Koko to finish eating within h hours
#  TakeAway: Learning how to apply binary search to find the optimal solution in a range of values, and how to calculate the required hours based on the eating speed.
#================================


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left = 1
        right = max(piles)

        def get_hour(speed):
            hours = 0
            for pile in piles:
                hours += (pile + speed-1)//speed
            return hours

        while left <= right:
            mid = (left+right)//2

            if left == right:
                return left
                
            if get_hour(mid) > h:
                left = mid +1
            else:
                right = mid