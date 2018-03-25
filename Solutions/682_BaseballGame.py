##############################################
## Author: I-No Liao                        ##
## Date of update: 2018/03/22               ##
## Description: Leetcode #682               ##
##############################################

# You're now a baseball game point recorder.
# 
# Given a list of strings, each string can be one of the 4 following types:
# 
# Integer (one round's score): Directly represents the number of points you get in this round.
# "+" (one round's score): Represents that the points you get in this round are the sum of the last two valid round's points.
# "D" (one round's score): Represents that the points you get in this round are the doubled data of the last valid round's points.
# "C" (an operation, which isn't a round's score): Represents the last valid round's points you get were invalid and should be removed.
# Each round's operation is permanent and could have an impact on the round before and the round after.
# 
# You need to return the sum of the points you could get in all the rounds.
# 
# Example 2:
# Input: ["5","-2","4","C","D","9","+","+"]
# Output: 27
# Explanation: 
# Round 1: You could get 5 points. The sum is: 5.
# Round 2: You could get -2 points. The sum is: 3.
# Round 3: You could get 4 points. The sum is: 7.
# Operation 1: The round 3's data is invalid. The sum is: 3.  
# Round 4: You could get -4 points (the round 3's data has been removed). The sum is: -1.
# Round 5: You could get 9 points. The sum is: 8.
# Round 6: You could get -4 + 9 = 5 points. The sum is 13.
# Round 7: You could get 9 + 5 = 14 points. The sum is 27.

import collections

class Solution(object):
    
    # @param ops, List[str]
    # @return, integer
    def calPoints(self, ops):
        
        # Sum: Score summation
        Sum = 0
        # Stack s1 stores the "Valid" round points
        s1 = collections.deque()

        for i in range(len(ops)):
            if ops[i] == "+":
                temp1 = s1.pop()
                temp2 = s1.pop()
                cur_round = temp1 + temp2
                Sum += cur_round
                s1.append(temp2) # Mind the append order
                s1.append(temp1) # Mind the append order
                s1.append(cur_round)

            elif ops[i] == "D":
                temp1 = s1.pop()
                cur_round = 2*temp1
                Sum += cur_round
                s1.append(temp1)
                s1.append(cur_round)

            elif ops[i] == "C":
                temp1 = s1.pop()
                Sum -= temp1

            else:
                Sum += int(ops[i])
                s1.append(int(ops[i]))

        return Sum

# Main
if __name__ == '__main__':
    
    myList = ["5","-2","4","C","D","9","+","+"]
    print( Solution().calPoints(myList) )
