#================================
# Working process:
#   1. Pair up parentheses with dictionary
#   2. If str[0] is not opening parentheses, return False
#   3. Iterate over str
#   4. If it is opening parentheses, append to a list stack
#   5. If it is not opening parenthesis, check if it is pair with the last element of pair dictionary
#   6. If not, return False
#   7. If loop succesfully ends, check if stack is empty
#   8. If it is, return True, otherwise, return False
# Issues: Code is not as pythonic and is hard to read
#================================


class Solution:
    def isValid(self, s: str) -> bool:

        pair = {'(':')','{':'}','[':']'}

        stack = []

        if s[0] not in pair:
            return False
        
        for i in s:
            if i in pair:
                stack.append(i)
            else:
                if stack != []:
                    if pair[stack[-1]] == i:
                        stack.pop()
                    else: return False
                else: return False
        
        if stack == []:
            return True
        else: return False