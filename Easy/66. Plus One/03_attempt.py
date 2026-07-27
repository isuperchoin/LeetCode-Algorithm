#================================
# Working process:
#   1. Substitue the last element of digits with the last element plus one
#   2. If the number becomes ten, substitute the number with 0 and add one to the previous element
#   3. If index [0] becomes ten, substitute number with 0 and add the whole list to list [1]
# Refinement: Index management became tidy and readable
# TakeAway: Learning how to iterate in reversed order
#================================


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:

        for i in reversed(range(len(digits))):
            digits[i] = digits[i]+1
            if digits[i] == 10:
               digits[i] = 0
            else:
                return digits

        return [1] + digits