#

# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
#
# Example 1:
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:
#
# Input: "cbbd"
# Output: "bb"


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # latonn's
        if len(set(s)) == 1:
            return s

        left, right, longest = 0, 0, 0
        dp = [[0] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            for j in range(i):
                dp[j][i] = (s[j] == s[i]) and ((i - j < 2) or dp[j+1][i-1])
                if dp[j][i] and longest < i - j + 1:
                    longest = i - j + 1
                    left, right = j, i
                # print(dp)
        return s[left: right + 1]

        # kamyu's
        # Manacher's Algorithm
        # http://leetcode.com/2011/11/longest-palindromic-substring-part-ii.html


if __name__ == '__main__':
    s = 'babad'
    print(Solution().longestPalindrome(s))

