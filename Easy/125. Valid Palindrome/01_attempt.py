#================================
# Working process:
#   1. Iterate over s and filter only lower case alphabets and numbers
#   2. append each of the letters into a list
#   3. Compare the list with reversed list
#   4. If they are equal, return True, else, return False
# TakeAway: Learning how to filter strings
#================================


class Solution:
    def isPalindrome(self, s: str) -> bool:

        filtered = []
        alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
        alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        num = '0123456789'

        for i in s:
            if i in alphabet_lower:
                filtered.append(i)
            elif i in alphabet_upper:
                filtered.append(alphabet_lower[alphabet_upper.index(i)])
            elif i in num:
                filtered.append(i)

        if filtered == filtered[::-1]:
            return True
        else:
            return False
            