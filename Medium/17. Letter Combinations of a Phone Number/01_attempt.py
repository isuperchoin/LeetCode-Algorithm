#================================
# Working process:
#   1. Create a mapping of digits to letters
#   2. Use depth-first search (DFS) to generate all combinations of letters based on the input digits
#   3. If the length of the current path is equal to the length of the input digits, add the path to the output list
#   4. Return the output list of letter combinations
# TakeAway: Understanding how to use DFS for generating combinations and the importance of backtracking
#================================


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        output = []
        mapping = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}

        if digits == "":
            return []
        
        def dfs(path, index):
            if len(path) == len(digits):
                output.append(path)
                return

            for i in mapping[digits[index]]:
                dfs(path + i, index +1)

            index -= 1


        dfs('',0)
        return output