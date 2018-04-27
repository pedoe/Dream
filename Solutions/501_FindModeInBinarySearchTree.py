##############################################
## Author: I-No Liao                        ##
## Date of update: 2018/04/17               ##
## Description: Leetcode #501               ##
##############################################

# Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.
# 
# Assume a BST is defined as follows:
# 
# The left subtree of a node contains only nodes with keys less than or equal to the node's key.
# The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
# Both the left and right subtrees must also be binary search trees.
# For example:
# Given BST [1,null,2,2],
#    1
#     \
#      2
#     /
#    2
# return [2].
# 
# Note: If a tree has more than one mode, you can return them in any order.
# 
# Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).

import collections
from Tree import TreeNode, BinaryTree

class Solution:
    # @param root: TreeNode
    # @return list[int]
    def findMode(self, root):
        # @param curr: TreeNode
        # @param LUT: dict
        # @return None
        def findModeHelper(curr, LUT):
            if curr is None:
                return None
            if LUT.get(curr.val) is None:
                LUT[curr.val] = 1
            else:
                LUT[curr.val] += 1
            
            findModeHelper(curr.left, LUT)
            findModeHelper(curr.right, LUT)
        
        if root is None:
            return []
        LUT = {}
        res = []
        findModeHelper(root, LUT)
        maxFreq = max(LUT.values())
        for item in LUT:
            if LUT[item] == maxFreq:
                res.append(item)
        return res

# Main
if __name__ == '__main__':
    nodes = [1, 'null', 2, 'null', 'null', 2]
    nodes = [1, 1, 2, 'null', 'null', 2]
    root = BinaryTree().makeTree(nodes, 0)
    print(BinaryTree().levelOrder(root))

    # findMode
    print(Solution().findMode(root))
