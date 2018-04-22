##############################################
## Author: I-No Liao                        ##
## Date of update: 2018/04/17               ##
## Description: Leetcode #110               ##
##############################################

# Given a binary tree, determine if it is height-balanced.
# 
# For this problem, a height-balanced binary tree is defined as:
# 
# a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
# 
# Example 1:
# 
# Given the following tree [3,9,20,null,null,15,7]:
# 
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Return true.
# 
# Example 2:
# 
# Given the following tree [1,2,2,3,3,null,null,4,4]:
# 
#        1
#       / \
#      2   2
#     / \
#    3   3
#   / \
#  4   4
# Return false.

import collections
from Tree import TreeNode, BinaryTree

# Time: O(n^2)
class Solution:
    # @param root: TreeNode
    # @return bool
    def isBalanced(self, root):
        if root is None:
            return True
        depth_l, depth_r = self.maxDepth(root.left), self.maxDepth(root.right)
        if abs(depth_l-depth_r) > 1:
            return False
        else:
            # Check if all subtrees are balanced
            return self.isBalanced(root.left) and self.isBalanced(root.right)
    
    # @param curr: TreeNode
    # @return int
    def maxDepth(self, curr):
        if curr is None:
            return 0
        if curr.left is None and curr.right is None:
            return 1
        else:
            return max(self.maxDepth(curr.left), self.maxDepth(curr.right)) + 1

# Good solution.
# Especially the getDepth() function.
# Time: O(n)
class kamyu104:
    # @param root: TreeNode
    # @return bool
    def isBalanced(self, root):
        return self.getDepth(root) >= 0

    # @param root: TreeNode
    # @return int 
    # return >= 0: Tree depth
    # return -1: Not balanced
    def getDepth(self, root):
        if root is None:
            return 0
        depth_l, depth_r = self.getDepth(root.left), self.getDepth(root.right)
        # If not balanced, return -1 to notice parent that one of or both of its subtree is not balanced.
        if abs(depth_l-depth_r) > 1 or depth_l < 0 or depth_r < 0:
            return -1
        # If valid, keep accumulate tree depth
        return max(depth_l, depth_r) + 1

# Main
if __name__ == '__main__':
    # nodes = [3, 9, 20, 'null', 'null', 15, 7]
    # nodes = [1, 2, 2, 3, 3, 'null', 'null', 4, 4]
    nodes = [1, 2, 2, 3, 3, 'null', 8, 4, 4, 'null', 'null', 'null', 'null', 'null', 10]
    root = BinaryTree().makeTree(nodes, 0)
    print(BinaryTree().levelOrder(root))

    # isBalancedDepth
    print(Solution().isBalanced(root))
    print(kamyu104().isBalanced(root))
