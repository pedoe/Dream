# Time:  O(m * n)
# Space: O(n)

# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers
# on the row below.
#
# For example, given the following triangle
#
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
#
# Note:
#
# Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in
# the triangle.


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # latonn's
        dp = [[] for _ in range(len(triangle))]
        dp[0] = triangle[0]
        tmp = []
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    tmp.append(dp[i-1][0] + triangle[i][j])
                elif j == len(triangle[i]) - 1:
                    tmp.append(dp[i-1][-1] + triangle[i][j])
                else:
                    tmp.append(min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j])
            dp[i] += tmp
            del tmp[:]
        return min(dp[-1])


if __name__ == '__main__':
    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    print(Solution().minimumTotal(triangle))

