#================================
# Working process:
#   1. Declare an empty list called output to store the subsets.
#   2. Define a nested function called backtrack that takes two parameters: start (the starting index for the current subset) and path (the current subset being constructed).
#   3. Inside the backtrack function, append a copy of the current path to the output list.
#   4. Use a for loop to iterate through the nums list starting from the start index.
#   5. For each element, append it to the path and recursively call backtrack with the next index (i+1) and the updated path.
#   6. After the recursive call, remove the last element from the path to backtrack and explore other subsets.
#   7. Call the backtrack function with the initial parameters (0, []) to start generating subsets.
#   8. Return the output list containing all subsets.
#  TakeAway: The backtracking approach efficiently generates all possible subsets of the input list by exploring each element and its combinations, ensuring that all subsets are captured in the output list.
#================================


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:

        output = []

        def backtrack(start, path):
            output.append(path[:])

            for i in range(start, len(nums)):
                path.append(nums[i])

                backtrack(i+1, path)

                path.pop()

        backtrack(0,[])

        return output

        