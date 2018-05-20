# Time:  O(m * n)
# Space: O(m + n)

# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
#
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right
# corner of the grid (marked 'Finish' in the diagram below).
#
# How many possible unique paths are there?
#
#
# Above is a 7 x 3 grid. How many possible unique paths are there?
#
# Note: m and n will be at most 100.
#
# Example 1:
#
# Input: m = 3, n = 2
# Output: 3
#
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Right -> Down
# 2. Right -> Down -> Right
# 3. Down -> Right -> Right
#
# Example 2:
#
# Input: m = 7, n = 3
# Output: 28


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # latonn's
        # there are (m+n-2) steps in total, arrange them in a different order
        # to get all possible unique paths
        total = m + n -2
        few = min(m-1, n-1)
        ans, i = 1, 1
        for nums in range(total, few, -1):
            ans = ans * nums / i
            i += 1

        return int(ans)

        # kamyu's
        # dp solution
        # if m < n:
        #     return self.uniquePaths(n, m)
        # ways = [1] * n
        #
        # for i in range(1, m):
        #     for j in range(1, n):
        #         ways[j] += ways[j - 1]
        #
        # return ways[-1]


if __name__ == '__main__':
    m, n = 7, 3
    print(Solution().uniquePaths(m, n))


