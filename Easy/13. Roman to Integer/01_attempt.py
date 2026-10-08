#================================
# Working process:
#   1. Make roman to int dictionary data
#   2. Iterate through s and add each of them to the variable 'output'
#   3. If smaller number comes before bigger one, subtract the smaller one from output
# TakeAway: Learning how to use dictionary data type
#================================


class Solution:
    def romanToInt(self, s: str) -> int:
        output = 0
        dict = {'I':1, 'V':5, 'X':10,'L':50,'C':100,'D':500, 'M':1000}
        for i in range(len(s)-1):
            if dict[s[i]] < dict[s[i+1]]:
                output -= dict[s[i]]
            else:
                output += dict[s[i]]

        output += dict[s[len(s)-1]]

        return output
        
        