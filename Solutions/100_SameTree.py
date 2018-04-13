##############################################
## Author: I-No Liao                        ##
## Date of update: 2018/04/10               ##
## Description: Leetcode #100               ##
##############################################

# Given two binary trees, write a function to check if they are the same or not.
# 
# Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
# 
# 
# Example 1:
# 
# Input:     1         1
#           / \       / \
#          2   3     2   3
# 
#         [1,2,3],   [1,2,3]
# 
# Output: true
# Example 2:
# 
# Input:     1         1
#           /           \
#          2             2
# 
#         [1,2],     [1,null,2]
# 
# Output: false
# Example 3:
# 
# Input:     1         1
#           / \       / \
#          2   1     1   2
# 
#         [1,2,1],   [1,1,2]
# 
# Output: false

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param p, TreeNode
    # @param q, TreeNode
    # @return boolean
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# Main
if __name__ == '__main__':
    n0 = TreeNode(1)
    n1 = TreeNode(2)
    n2 = TreeNode(3)
    n0.left, n0.right = n1, n2

    m0 = TreeNode(1)
    m1 = TreeNode(2)
    m2 = TreeNode(3)
    m0.left, m0.right = m1, m2

    print(Solution().isSameTree(n0, m0))
