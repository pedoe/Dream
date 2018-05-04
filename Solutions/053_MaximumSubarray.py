##############################################
## Author: I-No Liao                        ##
## Date of update: 2018/04/30               ##
## Description: Leetcode #53                ##
##############################################

# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# 
# Example:
# 
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:
# 
# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

import collections

class Solution_1(object):
    # @param nums: list[int]
    # @return int
    # Time: O(n^2)
    # Compute everything
    def maxSubArray(self, nums):
        result = []
        for i in range(len(nums)):
            subresult = []
            for j in range(i, len(nums)):
                if len(subresult) == 0:
                    subresult.append(nums[j])
                else:
                    # The index of subresult[j-i-1] is tricky =P
                    subresult.append(subresult[j-i-1]+nums[j])
            result.extend(subresult)
            print("========================================")
            print("subresult of i=", i, "is", subresult)
        print(result)
        return max(result)

class Solution_2:
    # @param nums: list[int]
    # @return int
    # Time: O(n)
    # Due to "contiguous" subarray, we consider max(current_idx_val, accumulated_val) each time.
    # Current_idx_val = An
    # Accumulated_val = A0 + A1 + ... + An
    # If Accumulated_val is less than Current_idx_val, then we start from Current_idx_val, else we keep accumulating.
    # In this manner, we avoid accumulating all possible summations. 
    # Once we found the current_idx_val is greater then accumulated_val, we stop accumulation from the very begining.
    def maxSubArray(self, nums):
        for i in range(1, len(nums), 1):
            nums[i] = max(nums[i-1]+nums[i], nums[i])
        return max(nums)
    
    # This avoids messing up the original nums
    # def maxSubArray(self, nums):
    #     dp = list(map(lambda x: x, nums))
    #     for i in range(1, len(nums), 1):
    #         dp[i] = max(dp[i-1]+nums[i], nums[i])
    #     return max(dp)


# Main
if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(Solution_1().maxSubArray(nums))
    print(Solution_2().maxSubArray(nums))
