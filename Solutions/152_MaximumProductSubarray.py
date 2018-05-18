##############################################
## Author: I-No Liao                        ##
## Date of update: 2018/05/11               ##
## Description: Leetcode #152               ##
##############################################

# Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.
# 
# Example 1:
# 
# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:
# 
# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

import collections

# Time Limit Exceeded
# Time: O(n!). It has C(n, 2) number of computations.
class Solution:
    # @param nums: list[int]
    # @return int
    def maxProduct(self, nums):
        dp = [[float("-inf") for _ in nums] for _ in nums]
        rowMax = [0 for _ in nums]
        for i in range(0, len(nums)):
            dp[i][i] = nums[i]
            for j in range(i+1, len(nums)):
                dp[i][j] = dp[i][j-1] * nums[j]
            rowMax[i] = max(dp[i])
        # return max(max(dp))
        # print(dp)
        return max(rowMax)

# Time: O(n)
class leetcode_sol_1:
    # @param nums: list[int]
    # @return int
    # Explanation:
    # num is the current nums[i] from 1 to end.
    # pos and neg are most positive and most negative multiplications in the previous calculation.
    # In each step: we consider pos = (current num, previous most positive result * current num, previous most negative result * current num)
    def maxProduct(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        ans = pos = neg = nums[0]
        for num in nums[1:]:
            pos, neg = max(num, pos*num, neg*num), min(num, pos*num, neg*num)
            ans = max(ans, pos)
            # print("ans = %d, pos = %d, neg = %d" %(ans, pos, neg))
        return ans

# Time: O(n)
# Same as leetcode_sol_1 except for using array.
# Detail explanation is provided.
class leetcode_sol_2:
    def maxProduct(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        ans, pos, neg = [None]*len(nums), [None]*len(nums), [None]*len(nums)
        ans[0] = pos[0] = neg[0] = nums[0]
        for i in range(1, len(nums)):
            pos[i] = max( nums[i], nums[i]*pos[i-1], nums[i]*neg[i-1] )
            neg[i]= min( nums[i], nums[i]*pos[i-1], nums[i]*neg[i-1] )
            ans[i] = max(ans[i-1], pos[i])
            print("pos =", pos)
            print("neg =", neg)
            print("ans =", ans[:i])
            print("ans[%d] = max(ans[%d], pos[%d]) = " %(i, i-1, i), ans[i])
            print("-----------------------------------------")
        return ans[-1]

# Main
if __name__ == '__main__':
    # print(Solution().maxProduct([2, 3, -2, 4]))
    # print(Solution().maxProduct([0, 2]))
    print(leetcode_sol_2().maxProduct([2, 3, -2, 4, 3, -1, -3]))
    print(leetcode_sol_2().maxProduct([-4, -3]))
    
