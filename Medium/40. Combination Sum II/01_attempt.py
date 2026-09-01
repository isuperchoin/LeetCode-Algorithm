#================================
# Working process:
#   1. We define a backtracking function that takes the starting index, the current path, and the current sum as parameters.
#   2. If the current sum equals the target, we add a copy of the path to the output list and return.
#   3. If the current sum exceeds the target, we return to avoid unnecessary calculations.
#   4. We iterate through the candidates from the starting index to the end, skipping duplicates to avoid repeated combinations.
#   5. We add each candidate to the path and recursively call the backtracking function with the next index and updated sum.
#   6. After the recursive call, we remove the last candidate from the path to backtrack and explore other combinations.
# TakeAway: Practicing how to utilize backtracking in generating combinations of numbers with a target sum, while handling duplicates in the input list.
#================================


class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        output = []
        candidates.sort()

        def backtrack(start, path, cur_sum):
            if cur_sum == target:
                output.append(path[:])
                return
            elif cur_sum > target:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue

                path.append(candidates[i])

                backtrack(i+1, path, cur_sum + candidates[i])

                path.pop()

        backtrack(0,[],0)

        return output