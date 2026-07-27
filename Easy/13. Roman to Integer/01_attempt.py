#================================
# Working process:
#   1. Make greek to int dictionary data
#   2. Iterate through s and add each of them to the variable 'output'
#   3. If smaller number comes before bigger one, subtract the smaller one from output
# TakeAway: Learning how to use dictionary data type
#================================


class Solution:
    def romanToInt(self, s: str) -> int:
        output = 0
        lib = {'I':1, 'V':5, 'X':10,'L':50,'C':100,'D':500, 'M':1000}
        for i in range(len(s)-1):
            if lib[s[i]] < lib[s[i+1]]:
                output -= lib[s[i]]
            else:
                output += lib[s[i]]

        output += lib[s[len(s)-1]]

        return output
        
        