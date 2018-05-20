# Time:  O(n * sqrt(n))
# Space: O(n)

# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...)
# which sum to n.
#
# For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # latonn's
        dp = [i for i in range(n+1)]
        dp[0], dp[1] = 0, 1
        for i in range(2, n+1):
            for j in range(1, int(i ** 0.5)+1):
                dp[i] = min(dp[i-j*j] + 1, dp[i])
        return dp[n]


if __name__ == '__main__':
    n = 7168
    print(Solution().numSquares(n))
