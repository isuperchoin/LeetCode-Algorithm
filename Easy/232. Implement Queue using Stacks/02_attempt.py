#================================
# Working process:
#   1. Set up two stacks: in_stack for push operations and out_stack for pop and peek operations.
#   2. For push operation, push the element onto the in_stack.
#   3. For pop and peek operations, check if out_stack is empty.
#      - If out_stack is empty, move all elements from in_stack to out_stack by popping from in_stack and pushing onto out_stack.
#      - If out_stack is not empty, simply pop or peek the top element from out_stack.
#   4. The empty operation checks if both in_stack and out_stack are empty.
#  Refinement: Reduced the time complextity of moving all the elements back and forth.
#              Used peek() method in pop() to avoid code duplication.
#  TakeAway: Learning how to use two stacks to implement a queue.
#================================


class MyQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []
        

    def push(self, x: int) -> None:
        self.in_stack.append(x)
        

    def pop(self) -> int:
        self.peek()
        return self.out_stack.pop()

        

    def peek(self) -> int:

#===============[attempt 1: Using for loop]====================
#
#        if not self.out_stack:
#           for i in range(len(self.in_stack)):
#               self.out_stack.append(self.in_stack.pop())
#
#=======[Changed to while loop for better readability]=========

        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]
        

    def empty(self) -> bool:
        if not self.in_stack and not self.out_stack:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()