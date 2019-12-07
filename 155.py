class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
    def push(self, x: int) -> None:
        self.stack.append(x)
        sorted(self.stack).reverse()

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
        else:
            return
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        temp = self.stack
        return sorted(temp)[0]

minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())
minStack.pop()
print(minStack.top())
print(minStack.getMin())