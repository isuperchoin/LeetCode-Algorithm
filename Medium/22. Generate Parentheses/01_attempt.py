#================================
# Working process:
#   1. Define a function generateParenthesis that takes an integer n as input, representing the number of pairs of parentheses to generate.
#   2. Initialize an empty list output to store the valid combinations of parentheses.
#   3. Define a recursive helper function dfs that takes the current path (list of characters), the count of open parentheses (open_count), and the count of closed parentheses (closed_count) as parameters.
#   4. In the dfs function:
#      - If both open_count and closed_count are equal to n, it means a valid combination of parentheses has been formed. Join the path list into a string and append it to the output list, then return.
#      - If open_count exceeds n or closed_count exceeds open_count, return to backtrack, as it indicates an invalid state.
#      - Append an open parenthesis "(" to the path, increment open_count, and recursively call dfs with the updated parameters.
#      - After returning from the recursive call, pop the last character from the path to backtrack and decrement the corresponding count (open_count or closed_count) based on the popped character.
#      - Append a closed parenthesis ")" to the path, increment closed_count, and recursively call dfs with the updated parameters.
#      - After returning from the recursive call, pop the last character from the path to backtrack and decrement the corresponding count (open_count or closed_count) based on the popped character
#   5. Call the dfs function with an empty path and counts initialized to 0
#   6. Return the output list containing all valid combinations of parentheses.
#  Issue: The current implementation may have a high time complexity due to the recursive nature of the dfs function, which explores all possible combinations of parentheses. 
#================================


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:

        output = []

        def dfs(path, open_count, closed_count):

            if open_count == closed_count == n:
                output.append("".join(path))
                return
            elif open_count > n or closed_count > open_count:
                return

            path.append("(")
            open_count += 1
            
            dfs(path, open_count, closed_count)

            if path.pop() == "(":
                open_count -= 1
            else:
                closed_count -= 1

            path.append(")")
            closed_count += 1

            dfs(path, open_count, closed_count)

            if path.pop() == "(":
                open_count -= 1
            else:
                closed_count -= 1
            
        dfs([],0, 0)
        return output
        