#================================
# Working process:
#   1. Create two stacks, one for the main stack and one for the minimum values
#   2. When pushing a value, check if the min_stack is empty
#   3. If it is, append the value to both stacks
#   4. If it is not, check if the value is less than or equal to the last value in the min_stack
#   5. If it is, append the value to both stacks
#   6. If it is not, append the last value in the min_stack to the min_stack(keeping the minimum value)
#   7. When popping a value, pop from both stacks
#   8. When getting the top value, return the last value in the main stack
#   9. When getting the minimum value, return the last value in the min_stack
# TakeAway: Learning how to deal with stacks, use two stacks to keep track of the minimum value in a stack and using class to create a stack data structure
#================================


class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, value: int) -> None:
        self.stack.append(value)
        if self.min_stack:
            if value <= self.min_stack[-1]:
#Used a comparison opperator instead of .min() built-in function because I'm basically dealing with not a list but a stack
                self.min_stack.append(value)
            else:
                self.min_stack.append(self.min_stack[-1])
        else:
            self.min_stack.append(value)
        

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]