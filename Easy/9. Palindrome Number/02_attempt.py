#================================
# Working process:
#   1. Turn the integer into string
#   2. Check if the string is identical to the reversed string
# Refinement: More simple and readable code
# TakeAway: Learning how to slice and reverse string
#================================


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False