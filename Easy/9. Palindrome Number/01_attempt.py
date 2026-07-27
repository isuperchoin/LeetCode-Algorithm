#================================
# Working process:
#   1. Turn the integer into list
#   2. Check if the list is identical to the reversed list
# Issue: Unnecessaryly complex code
#================================


class Solution:
    def isPalindrome(self, x: int) -> bool:
        letters = list(str(x))
        letters_backward = list(reversed(letters))
        if letters == letters_backward:
            return True
        else:
            return False