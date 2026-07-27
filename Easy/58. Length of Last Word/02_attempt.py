#================================
# Working process:
#   1. Iterate over s in reversed order
#   2. If I walk into space, check if count is zero or not
#   3. If not zero, increase count variable
#   4. If it's not space, increase count by one
#   5. Return count
# Refinement: Replaced unnecessary list with count variable
# TakeAway: Learning to choose better tools for each situation
#================================


class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        count = 0

        for i in reversed(s):
            if i == ' ':
                if count != 0:
                    return count
            else: count += 1

        return count   