# Time:  O(1), amortized
# Space: O(n)

# Implement the following operations of a queue using stacks.
#
# push(x) -- Push element x to the back of queue.
# pop() -- Removes the element from in front of queue.
# peek() -- Get the front element.
# empty() -- Return whether the queue is empty.
#
# Notes:
# You must use only standard operations of a stack -- which means only
# push to top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, stack may not be supported natively. You
# may simulate a stack by using a list or deque (double-ended queue), as
# long as you use only standard operations of a stack.
# You may assume that all operations are valid (for example, no pop or
# peek operations will be called on an empty queue).


class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1, self.s2 = [], []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.s1.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[len(self.s2) - 1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.s1 and not self.s2

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


if __name__ == '__main__':
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    obj.push(3)
    print(obj.peek())
    print(obj.pop())
    print(obj.pop())
    print(obj.empty())
    print(obj.pop())
    print(obj.empty())
