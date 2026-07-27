#================================
# Working process:
#   1. Loop in range of the shortest element of strs
#   2. Iterate over strs and compare if strs[0]'s ith letter is equal to every other elements' ith letter
#   3. If not equal one is found return what we have by slicing
#   4. If the loop succesfully ends, return what we have by slicing
# Refinement: No more unnecessry lists
# TakeAway: Learning how to slice list
#================================


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        for i in range(len(min(strs,key=len))):

            for s in strs:
                if s[i] != strs[0][i]:
                    return strs[0][:i]
        
        return strs[0][:len(min(strs,key=len))]