##############################################
## Author: I-No Liao                        ##
## Date of update: 2018/03/20               ##
## Description: Leetcode #225               ##
##############################################

# Implement the following operations of a stack using queues.
# 
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# empty() -- Return whether the stack is empty.
# Notes:
# You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
# Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
# You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).

import collections

class Queue(object):

    def __init__(self):
        # https://docs.python.org/2/library/collections.html
        self.data = collections.deque()

    def push(self, x):
        self.data.append(x)

    def pop(self):
        return self.data.popleft()

    def peek(self):
        return self.data[0]

    def size(self):
        return len(self.data)

    def empty(self):
        return len(self.data) == 0

# Time: push O(1), pop O(n), top O(1)
# Space: O(n)
class Stack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q_ = Queue()
        self.top_ = None

    # @param x, integer
    # @return, void
    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.q_.push(x)
        self.top_ = x
        
    # @param
    # @return, integer
    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        # pop and push until the last element is popped from queue
        # keep updating stack's top
        for i in range(self.q_.size() - 1):
            self.top_ = self.q_.pop()
            self.q_.push(self.top_)
        return self.q_.pop()
     
    # @return, integer
    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.top_
    
    # @return, boolean
    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.q_.empty()
        
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

# Main
if __name__ == '__main__':
    
    s1 = Stack()
    s1.push(1) 
    s1.push(2) 
    s1.push(3) 
    s1.push(4) 
    s1.push(5) 
    
    while s1.empty() != True:
        print( s1.pop() )

