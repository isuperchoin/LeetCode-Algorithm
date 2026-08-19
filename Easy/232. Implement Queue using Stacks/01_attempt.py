#================================
# Working process:
#   1. Set up two stacks
#   2. For push operation, push the element onto the first stack.
#   3. For pop and peek operations, move all elements from the first stack to the second stack except for the last element.
#   4. Pop or peek the last element from the first stack.
#   5. Move all elements back from the second stack to the first stack.
#  Issue: The pop and peek operations have a time complexity of O(n) due to the need to move elements between stacks.
#         Also, redundant code for moving elements between stacks.
#================================


class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x: int) -> None:
        self.stack1.append(x)

        

    def pop(self) -> int:
        for i in range(len(self.stack1)-1):
            self.stack2.append(self.stack1.pop())
        output = self.stack1.pop()
        for i in range(len(self.stack2)):
            self.stack1.append(self.stack2.pop())
        return output


    def peek(self) -> int:
        for i in range(len(self.stack1)-1):
            self.stack2.append(self.stack1.pop())
        output = self.stack1[-1]
        for i in range(len(self.stack2)):
            self.stack1.append(self.stack2.pop())
        return output
        

    def empty(self) -> bool:
        if self.stack1:
            return False
        else:
            return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()