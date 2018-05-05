# Time:  ctor:   O(n),
#        lookup: O(1)
# Space: O(n)

# Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
#
# Example:
# Given nums = [-2, 0, 3, -5, 2, -1]
#
# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3
# Note:
# You may assume that the array does not change.
# There are many calls to sumRange function.


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.dp = [0 for _ in range(len(nums) + 1)]
        self.dp[0] = 0
        for i in range(1, len(nums) + 1):
            self.dp[i] = self.dp[i - 1] + nums[i - 1]
        print(self.dp)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.dp[j + 1] - self.dp[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

if __name__ == '__main__':
    nums = [-2, 0, 3, -5, 2, -1]
    obj = NumArray(nums)
    print(obj.sumRange(0, 5))
