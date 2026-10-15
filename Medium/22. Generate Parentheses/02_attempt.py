#================================
# Working process:
#   1. Define a function generateParenthesis that takes an integer n as input, representing the number of pairs of parentheses to generate.
#   2. Initialize an empty list output to store the valid combinations of parentheses.
#   3. Define a recursive helper function dfs that takes the current path (list of characters), the count of open parentheses (open_count), and the count of closed parentheses (closed_count) as parameters.
#   4. In the dfs function:
#      - If both open_count and closed_count are equal to n, it means a valid combination of parentheses has been formed. Join the path list into a string and append it to the output list, then return.
#      - If open_count is less than n, append an open parenthesis "(" to the path, increment open_count, and recursively call dfs with the updated parameters. After returning from the recursive call, pop the last character from the path to backtrack and decrement open_count.
#      - If closed_count is less than open_count, append a closed parenthesis ")" to the path, increment closed_count, and recursively call dfs with the updated parameters. After returning from the recursive call, pop the last character from the path to backtrack and decrement closed_count.
#   5. Call the dfs function with an empty path and counts initialized to 0
#   6. Return the output list containing all valid combinations of parentheses.
#  Refinement: The current implementation has been refined to simplify the backtracking process by directly popping the last character from the path after each recursive call, eliminating the need for conditional checks on the popped character. This makes the code cleaner and easier to understand.
#  Takeaway: The refined implementation maintains the same logic and functionality as the previous version but improves code readability and maintainability by simplifying the backtracking process.
#================================


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:

        output = []

        def dfs(path, open_count, closed_count):

            if open_count == closed_count == n:
                output.append("".join(path))
                return

            if open_count < n:
                path.append("(")
                open_count += 1
                
                dfs(path, open_count, closed_count)

                path.pop()
                open_count -= 1

            if closed_count < open_count:
                path.append(")")
                closed_count += 1

                dfs(path, open_count, closed_count)

                path.pop()
                closed_count -= 1
            
        dfs([],0, 0)
        return output
        