#================================
# Working process:
#   1. Pair up parentheses with dictionary
#   2. If s[0] is not opening parenthesis, return False
#   3. Iterate over string s
#   4. If it is opening parentheses, append to a list stack
#   5. If it is not opening parenthesis, check if it matches the top element of the stack
#   6. If not, return False
#   7. After the loop, check if stack is empty
#   8. If it is, return True, otherwise, return False
# Refinement: Tidy conditions structure and more pythonic codes
# TakeAway: Learning how to use list as a boolean and stack algorithm
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
                if stack and pair[stack[-1]] == i:

                    stack.pop()

                else:
                    return False
        
        return not stack