#================================
# Working process:
#   1. Declare an empty list called output to store the combinations that sum up to the target.
#   2. Define a nested function called backtrack that takes two parameters: start (the starting index for the current combination) and path (the current combination being constructed).
#   3. Inside the backtrack function, check if the sum of the current path equals the target. If it does, append a copy of the current path to the output list and return.
#   4. If the sum of the current path exceeds the target, return to backtrack and explore other combinations.
#   5. Use a for loop to iterate through the candidates list starting from the start index.
#   6. For each element, check if adding it to the current path would exceed the target. If it does, skip to the next iteration.
#   7. If it doesn't exceed the target, append the element to the path and recursively call backtrack with the same index (i) to allow for repeated use of the same element and the updated path.
#   8. After the recursive call, remove the last element from the path to backtrack and explore other combinations.
#   9. Call the backtrack function with the initial parameters (0, []) to start generating combinations.
#   10. Return the output list containing all combinations that sum up to the target.
#  Issue: The current implementation checks the sum of the path multiple times, which can be inefficient.
#================================


class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        output = []
        def backtrack(start, path):
            if sum(path) == target:
                output.append(path[:])
                return
            elif sum(path) > target:
                return

            for i in range(start, len(candidates)):
                if sum(path)+ candidates[i] > target:
                    continue

                path.append(candidates[i])

                backtrack(i, path)

                path.pop()

        backtrack(0,[])

        return output