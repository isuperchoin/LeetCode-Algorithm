#================================
# Working process:
#   1. Substitue the last element of digits with the last element plus one
#   2. If the number becomes ten, substitute the number with 0 and add one to the previous element
#   3. If index [0] becomes ten, substitute number with 0 and add the whole list to list [1]
# Refinement: Did the actual alorithm
# Issue: Code is hard to read and index management is messy
#================================


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:

        for i in range(1, len(digits)+1):
            digits[len(digits)-i] = digits[len(digits)-i]+1
            if digits[len(digits)-i] == 10:
               digits[len(digits)-i] = 0
               if len(digits)-i == 0:
                return [1,] + digits
            else:
                return digits 