#================================
# Working process:
#  Similar to the previous implementation, but instead of calculating the sum of the path multiple times, we maintain a running sum (cur_sum) that is updated as we add or remove elements from the path.
# Refinement: This approach avoids the inefficiency of repeatedly calculating the sum of the path, making it more efficient for larger input sizes.
# TakeAway: Learning to maintain a running sum during backtracking.
#================================


class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        output = []
        def backtrack(start, path, cur_sum):
            if cur_sum == target:
                output.append(path[:])
                return
            elif cur_sum > target:
                return

            for i in range(start, len(candidates)):
                if cur_sum + candidates[i] > target:
                    continue

                path.append(candidates[i])

                backtrack(i, path, cur_sum + candidates[i])

                path.pop()

        backtrack(0,[],0)

        return output