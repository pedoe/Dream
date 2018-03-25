##############################################
## Author: I-No Liao                        ##
## Date of update: 2018/03/22               ##
## Description: Leetcode #621               ##
##############################################

# Given a char array representing tasks CPU need to do. 
# It contains capital letters A to Z where different letters represent different tasks.
# Tasks could be done without original order. 
# Each task could be done in one interval. 
# For each interval, CPU could finish one task or just be idle.
# 
# However, there is a non-negative cooling interval n that means between two same tasks, 
# there must be at least n intervals that CPU are doing different tasks or just be idle.
# 
# You need to return the least number of intervals the CPU will take to finish all the given tasks.
# 
# Example 1:
# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
# 
# INo: Same tasks are allowed to emerge if the interval tasks b/w them is >= n

import collections

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        dictionary = collections.defaultdict(int)
        max_count = 0
        
        # Count the frequency of tasks
        # Record the most frequent task's value: max_count
        for task in tasks:
            dictionary[task] += 1
            max_count = max(max_count, dictionary[task])

        # Compute result
        # max_count-1 = number of boxes of train
        # 1+n = Head + n intervals = number of tasks in a box
        result = (max_count-1) * (1+n)

        # Check if the interval is enough for all other tasks
        for task_count in dictionary.values():
            if task_count == max_count:
                result += 1
        
        # return result: If all tasks can be placed into the gap b/w the heads of each box
        # return len(tasks): If # of places in all the boxes can not contain total # of tasks
        return max(result, len(tasks))

# Main
if __name__ == '__main__':
    
    tasks = ["A","A","A","B","B","B"]
    # tasks = ["A","A","A","B","B","C"]
    # tasks = ["A","A","B","D","E","F"]
    n = 2
    
    print( Solution().leastInterval(tasks, n) )
