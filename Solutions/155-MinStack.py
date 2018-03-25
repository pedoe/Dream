# Time:  O(n)
# Space: O(1)

# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
#
# Example:
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.


class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = 0
        self.stack = []

    # latonn's
    # def push(self, x):
    #     """
    #     :type x: int
    #     :rtype: void
    #     """
    #     if not self.stack:
    #         self.min = x
    #     elif x < self.min:
    #         self.min = x
    #     self.stack.append(x)
    #
    # def pop(self):
    #     """
    #     :rtype: void
    #     """
    #     if self.stack[-1] == self.min:
    #         self.min = self.stack[0]
    #         for i in range(len(self.stack) - 1):
    #             if self.stack[i] < self.min:
    #                 self.min = self.stack[i]
    #     del self.stack[-1]
    #
    # def top(self):
    #     """
    #     :rtype: int
    #     """
    #     return self.stack[-1]

    # kamyu's
    # @param x, an integer
    # @return an integer
    def push(self, x):
        if not self.stack:
            self.stack.append(0)
            self.min = x
        else:
            self.stack.append(x - self.min)
            if x < self.min:
                self.min = x
        print(self.stack)

    # @return nothing
    def pop(self):
        x = self.stack.pop()
        if x < 0:
            self.min = self.min - x

    # @return an integer
    def top(self):
        x = self.stack[-1]
        if x > 0:
            return x + self.min
        else:
            return self.min

    def getMin(self):
        """
        :rtype: int
        """
        return self.min

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(3)
    minStack.push(2)
    minStack.push(5)
    minStack.push(1)
    minStack.push(0)
    print(minStack.top())
    print(minStack.getMin())
    minStack.pop()
    print(minStack.getMin())
    print(minStack.top())

