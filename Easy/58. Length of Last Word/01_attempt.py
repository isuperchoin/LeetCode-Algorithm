#================================
# Working process:
#   1. Iterate over s in reversed order and append it to temp list
#   2. If I walk into space, check if we have space in temp
#   3. If we do, empty the temp list
#   4. Else, return the length of temp list
#  Issue: Unnecessary list
#================================


class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        temp = []
        for i in reversed(s):
            if i == ' ':
                if ' ' in temp or temp == []:
                    temp = []
                else: return len(temp)
            else: temp.append(i)

        return len(temp)