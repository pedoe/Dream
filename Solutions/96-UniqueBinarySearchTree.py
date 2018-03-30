# Time:  O(n)
# Space: O(1)

# Given n, how many structurally unique BST's (binary search trees) that store values 1...n?
#
# For example,
# Given n = 3, there are a total of 5 unique BST's.
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3


class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # latonn's 1st version
        # Time:  O(n^2)
        # Space: O(n)
        # if n == 1:
        #     return 1
        #
        # ans = 0
        # for i in range(1, n + 1):
        #     if i in (1, n):
        #         ans += self.numTrees(n - 1)
        #     else:
        #         ans += self.numTrees(i - 1) * self.numTrees(n - i)
        # return ans

        # latonn's 2nd version
        # Time:  O(n^2)
        # Space: O(n)
        # ans = []
        # ans.append(1)
        # ans.append(1)
        #
        # for i in range(2, n + 1):
        #     tmp = 0
        #     for j in range(1, i + 1):
        #         tmp += ans[j - 1] * ans[i - j]
        #     ans.append(tmp)
        # return ans[n]

        # kamyu's
        # Time:  O(n)
        # Space: O(1)
        # Catalan Number
        # https: // en.wikipedia.org / wiki / Catalan_number
        if n == 0:
            return 1

        def combination(n, k):
            count = 1
            # C(n, k) = (n) / 1 * (n - 1) / 2 ... * (n - k + 1) / k
            for i in range(1, k + 1):
                count = count * (n - i + 1) / i
            return int(count)

        return combination(2 * n, n) - combination(2 * n, n - 1)


if __name__ == '__main__':
    n = 3
    print(Solution().numTrees(n))
