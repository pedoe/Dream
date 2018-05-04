##############################################
## Author: I-No Liao                        ##
## Date of update: 2018/04/30               ##
## Description: Leetcode #70                ##
##############################################

# You are climbing a stair case. It takes n steps to reach to the top.
# 
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# 
# Note: Given n will be a positive integer.
# 
# Example 1:
# 
# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:
# 
# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

import collections

# I-No's solution
# Time: O(n)
# I enumerate from n = 1 to n = 5 and conclude the formula: An = An-2 + An-1
class Solution(object):
    # @param n: int
    # @return int
    def climbStairs(self, n):
        result = [1, 2]
        if n == 1:
            return result[0]
        if n == 2:
            return result[1]
        for i in range(2, n):
            result.append(result[i-2]+result[i-1])
        return result[n-1]

# kamyu104's solution
# Time: O(2^n)
# Time limit exceeded.
# However, the recursion is insightful.
class kamyu104:
    # @param n: int
    # @return int
    def climbStairs(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n-2) + self.climbStairs(n-1)


# Main
if __name__ == '__main__':
    print(Solution().climbStairs(6))
    print(kamyu104().climbStairs(6))
