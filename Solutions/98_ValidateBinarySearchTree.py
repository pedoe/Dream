##############################################
## Author: I-No Liao                        ##
## Date of update: 2018/04/18               ##
## Description: Leetcode #98                ##
##############################################

# Given a binary tree, determine if it is a valid binary search tree (BST).
# 
# Assume a BST is defined as follows:
# 
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
# Example 1:
#     2
#    / \
#   1   3
# Binary tree [2,1,3], return true.
# Example 2:
#     1
#    / \
#   2   3
# Binary tree [1,2,3], return false.

import collections
from Tree import TreeNode, BinaryTree

# Time: O(2n) = O(n) for inorderTraversal and O(n) for checking sorted list
class Solution:
    # @param root: TreeNode
    # @return bool
    def isValidBST(self, root):
        # @param curr: TreeNode
        # @param res: list[int]
        # @return list[int]
        def inorderTraversal(curr, res):
            if curr is None:
                return res
            inorderTraversal(curr.left, res)
            res.append(curr.val)
            inorderTraversal(curr.right, res)
            return res

        if root is None:
            return True
        sortedList = inorderTraversal(root, [])
        # If sortedList is sorted, return True; otherwise, return False
        for i in range(len(sortedList)-1):
            if sortedList[i+1]-sortedList[i] <= 0:
                return False
        return True

class kamyu104:
    # @param root: TreeNode
    # @return bool
    def isValidBST(self, root):
        def isValidBSTRecu(root, low, high):
            if root is None:
                return True
            return low < root.val and high > root.val \
                    and isValidBSTRecu(root.left, low, root.val) \
                    and isValidBSTRecu(root.right, root.val, high)

        return isValidBSTRecu(root, float("-inf"), float("inf"))

# Use morris traversal to solve problem.
class morris:
    # @param curr: TreeNode
    # @return list[int]
    # Time: O(n)
    # Space: O(1)
    # Based on morris inorder traversal, add prev node to check BST validity.
    def isValidBST(self, root):
        predecessor, prev, curr = None, None, root
        while curr:
            if curr.left is None:
                if prev and prev.val >= curr.val:
                    return False
                prev = curr
                curr = curr.right
            else:
                predecessor = curr.left
                while predecessor.right and predecessor.right != curr:
                    predecessor = predecessor.right
                
                if predecessor.right is None:
                    predecessor.right = curr
                    curr = curr.left
                
                else:
                    if prev and prev.val >= curr.val:
                        return False
                    predecessor.right = None
                    prev = curr
                    curr = curr.right
        return True

# Main
if __name__ == '__main__':
    # nodes = [2, 1, 3]
    # nodes = [1, 2, 3]
    nodes = [10, 5, 15, 'null', 'null', 6, 20]
    root = BinaryTree().makeTree(nodes, 0)
    print(BinaryTree().levelOrder(root))
    # print(BinaryTree().morrisInorder(root))

    # isValidBST?
    print(Solution().isValidBST(root))
    print(kamyu104().isValidBST(root))
    print(morris().isValidBST(root))
