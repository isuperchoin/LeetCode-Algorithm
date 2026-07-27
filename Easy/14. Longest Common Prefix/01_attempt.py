#================================
# Working process:
#   1. Loop in range of the shortest element of strs
#   2. Iterate over strs and compare if strs[0]'s ith letter is equal to every other elements' ith letter
#   3. If not equal one is found return what we have
#   4. If the loop succesfully ends, append the letter to output list
#   5. Join the output list
#   6. Return the string
#  Issue: Unnecessary data types
#================================


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        output = []

        for i in range(len(min(strs, key=len))):
            for s in strs:
                if s[i] != strs[0][i]:
                    return "".join(output)
            output.append(s[i])
        
        return "".join(output)
              