##############################################
## Author: I-No Liao                        ##
## Date of update: 2018/05/01               ##
## Description: Leetcode #338               ##
##############################################

# Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.
# 
# Example:
# For num = 5 you should return [0,1,1,2,1,2].
# 
# Follow up:
# 
# It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
# Space complexity should be O(n).
# Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
# Credits:
# Special thanks to @ syedee for adding this problem and creating all test cases.

import collections

# Time: O(n*sizeof(integer))
class Solution(object):
    # @param num: int
    # @return list[int]
    def countBits(self, num):
        result = []
        for i in range(num+1):
            result += [self.oneCounter(self.decimalToBinary_1(i))]
        return result
    
    # @param num: int
    # @return list[int]
    def decimalToBinary_1(self, num):
        quotient = int(num/2)
        remainder = [num%2]
        # print(remainder)
        while quotient != 0:
            remainder += [quotient%2]
            quotient = int(quotient/2)
        return remainder[::-1]
    
    # @param num: int
    # @return list[str]
    # DP algorithm: Reuse the previous computed results.
    def decimalToBinary_2(self, num):
        result = ['0']
        for i in range(1, num+1):
            res_i = '1' if i == 1 else result[int(i/2)] + str(i%2)
            result += [res_i]
        return result

    # @param binaryNum: list[int]
    # @return int
    def oneCounter(self, binaryNum):
        count = 0
        for num in binaryNum:
            count = count + 1 if num == 1 else count
        return count

# Time: O(n)
# 0/2 = 0...0 (result[0]) (000)
# 1/2 = 0...1 (result[1] = result[1/2] + 1%2 = result[0] + 1 = (Prefix digits are from previous calculation and LSB is 1%2) (00 1)
# 2/2 = 1...0 (result[2] = result[2/2] + 2%2 = result[1] + 0 = (Prefix digits are from previous calculation and LSB is 2%2) (01 0)
# 3/2 = 1...0 (result[3] = result[3/2] + 3%2 = result[1] + 1 = (Prefix digits are from previous calculation and LSB is 3%2) (01 1)
# 4/2 = 2...0 (result[4] = result[4/2] + 4%2 = result[2] + 0 = (Prefix digits are from previous calculation and LSB is 4%2) (10 0)
# 5/2 = 2...1 (result[5] = result[5/2] + 5%2 = result[2] + 1 = (Prefix digits are from previous calculation and LSB is 5%2) (10 1)
# 6/2 = 3...0 (result[6] = result[6/2] + 6%2 = result[3] + 0 = (Prefix digits are from previous calculation and LSB is 6%2) (11 0)
# 7/2 = 3...1 (result[7] = result[7/2] + 7%2 = result[3] + 1 = (Prefix digits are from previous calculation and LSB is 7%2) (11 1)
# and so on.
# Hence, we observe that result[n] = result[int(n/2)] + n%2 = reuse previous result + current last bit. It is dynamic programming!
class DP:
    # @param num: int
    # @return list[int]
    def countBits(self, num):
        result = [0]
        for i in range(1, num+1):
            res_i = result[int(i/2)] + i%2
            result += [res_i]
        return result

# Main
if __name__ == '__main__':
    print(Solution().decimalToBinary_1(12))
    print(Solution().decimalToBinary_2(16))
    print(Solution().oneCounter([1, 1, 0, 0]))
    print(Solution().countBits(5))
    print(DP().countBits(5))
