##############################################
## Author: I-No Liao                        ##
## Date of update: 2018/05/10               ##
## Description: Leetcode #322               ##
##############################################

# You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
# 
# Example 1:
# coins = [1, 2, 5], amount = 11
# return 3 (11 = 5 + 5 + 1)
# 
# Example 2:
# coins = [2], amount = 3
# return -1.
# 
# Note:
# You may assume that you have an infinite number of each kind of coin.

import collections

class Solution:
    # @param coins: list[int]
    # @param amount: int
    # @return int
    # dp[i] = min( dp[i], dp[i-coins[j]] + 1 )
    # dp[i] is the fewest number of coins to make up i amount of money.
    # reference: http://www.cnblogs.com/grandyang/p/5138186.html
    def coinChange(self, coins, amount):
        # anount + 1 is the upper bound: 1 cent coins combination = amount < amount + 1 = upper bound
        dp = [ amount + 1 for _ in range(amount+1) ]
        dp[0] = 0
        for i in range(1, amount+1):
            for j in range(0, len(coins)):
                if coins[j] <= i:
                    dp[i] = min( dp[i], dp[i-coins[j]] + 1 )
        return dp[amount] if dp[amount] <= amount else -1

# Main
if __name__ == '__main__':
    print(Solution().coinChange([1, 2, 5], 11))
    # print(Solution().coinChange([2], 3))
    # print(Solution().coinChange([186,419,83,408], 6249))
