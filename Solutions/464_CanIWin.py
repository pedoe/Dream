##############################################
## Author: I-No Liao                        ##
## Date of update: 2018/05/11               ##
## Description: Leetcode #464               ##
##############################################

# In the "100 game," two players take turns adding, to a running total, any integer from 1..10. The player who first causes the running total to reach or exceed 100 wins.
# 
# What if we change the game so that players cannot re-use integers?
# 
# For example, two players might take turns drawing from a common pool of numbers of 1..15 without replacement until they reach a total >= 100.
# 
# Given an integer maxChoosableInteger and another integer desiredTotal, determine if the first player to move can force a win, assuming both players play optimally.
# 
# You can always assume that maxChoosableInteger will not be larger than 20 and desiredTotal will not be larger than 300.
# 
# Example
# 
# Input:
# maxChoosableInteger = 10
# desiredTotal = 11
# 
# Output:
# false
# 
# Explanation:
# No matter which integer the first player choose, the first player will lose.
# The first player can choose an integer from 1 up to 10.
# If the first player choose 1, the second player can only choose integers from 2 up to 10.
# The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
# Same with other integers chosen by the first player, the second player will always win.

import collections

# https://leetcode.com/problems/can-i-win/discuss/95319/Python-solution-with-detailed-explanation
# State: current set of allowed values. Because so_far defines current state, and so_far = sum(all allowed) - sum(used allowed values) = current allowed values. So current state = current allowed values.
# Condition: if max(allowed) + so_far >= Target, then current player wins; otherwise, sweep current allowed value one by one, and recursively call other player.
# Time: O(N*2^N), 2^N is due to C(N,1)+C(N,2)+...+C(N,k) = 2^N for each sweep of current allowed values. N is number of sweep the function needs.
class leetcode_sol_1(object):
    # @param allowed: list[int]
    # @param target, so_far: int
    # @param cache: dict (chache store every states with key=states and value=bool)
    # @return bool
    def helper(self, allowed, target, so_far, cache):
        if len(allowed) == 0:
            return False
        state = tuple(allowed)
        if state in cache:
            return cache[state]
        else:
            # Set current state to False first and check if there is any chance that current state is true.
            cache[state] = False
            if max(allowed) + so_far >= target:
                cache[state] = True
            else:
                # Based on current state (current allowed values), sweep each allowed value for current player and check if he wins.
                for x in allowed:
                    # new_allowed is for the next player. x is picked by current player and y is for the next player.
                    new_allowed = [y for y in allowed if x!=y]
                    # If the next player must fail the game, then current player wins.
                    if self.helper(new_allowed, target, so_far+x, cache) ==  False:
                        cache[state] = True
                        break
            return cache[state]
    
    def canIWin(self, maxChoosableInteger, desiredTotal):
        allowed = [x for x in range(1, maxChoosableInteger+1)]
        if sum(allowed) < desiredTotal:
            return False
        return self.helper(allowed, desiredTotal, 0, {})

from collections import defaultdict
class leetcode_sol_2:
    def canIWin(self, maxChoosableInteger, desiredTotal):        
        ## https://leetcode.com/problems/can-i-win/discuss/95277/java-solution-using-hashmap-with-detailed-explanation
        ## http://bgmeow.xyz/2017/01/18/LeetCode-464/
        ## http://www.cnblogs.com/grandyang/p/6103525.html
        
        # Player 1 must win when choose a number which is larger than desireTotal
        if maxChoosableInteger >= desiredTotal:
            return True
       
        # Sum of 1 to maxChoosableInteger < desiredTotal: False
        if (maxChoosableInteger + 1) * maxChoosableInteger / 2 < desiredTotal:
            return False
        
        states = defaultdict(bool)
        return self.dfs(maxChoosableInteger, desiredTotal, 0, states)
    
    ## used表示上一次选的是哪一个数字
    def dfs(self, limit, total, used, states):
        
        if used in states:
            return states[used]
        
        for i in range(limit):
            key = 1 << i ## key = 2^i
            if key & used == 0:
                ## 在本轮循环中当前选的数字就是i + 1
                ## 如果当前选了i + 1能赢或者对手在下一次递归中不能赢
                ## 说明本次递归能赢
                if i + 1 >= total or not self.dfs(limit, total - (i + 1), key | used, states):
                    states[used] = True
                    return True
        
        states[used] = False
        return False

# Main
if __name__ == '__main__':
    print(leetcpde_sol_1().canIWin(10, 11))
    print(leetcode_sol_1().canIWin(10, 30))
