##############################################
## Author: I-No Liao                        ##
## Date of update: 2018/04/12               ##
## Description: Leetcode #623               ##
##############################################

# Given the root of a binary tree, then value v and depth d, you need to add a row of nodes with value v at the given depth d. The root node is at depth 1.
# 
# The adding rule is: given a positive integer depth d, for each NOT null tree nodes N in depth d-1, create two tree nodes with value v as N's left subtree root and right subtree root. And N's original left subtree should be the left subtree of the new left subtree root, its original right subtree should be the right subtree of the new right subtree root. If depth d is 1 that means there is no depth d-1 at all, then create a tree node with value v as the new root of the whole original tree, and the original tree is the new root's left subtree.
# 
# Example 1:
# Input: 
# A binary tree as following:
#        4
#      /   \
#     2     6
#    / \   / 
#   3   1 5   
# 
# v = 1
# 
# d = 2
# 
# Output: 
#        4
#       / \
#      1   1
#     /     \
#    2       6
#   / \     / 
#  3   1   5   
# 
# Example 2:
# Input: 
# A binary tree as following:
#       4
#      /   
#     2    
#    / \   
#   3   1    
# 
# v = 1
# 
# d = 3
# 
# Output: 
#       4
#      /   
#     2
#    / \    
#   1   1
#  /     \  
# 3       1
# Note:
# The given d is in range [1, maximum depth of the given tree + 1].
# The given binary tree has at least one tree node.

import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, TreeNode
    # @param v, d, int
    # @return TreeNode
    def addOneRow(self, root, v, d):
        if root is None:
            return root
        # Insert node to d = 0 (new root) @ d == 1
        if d-1 == 0:
            root, root.left = TreeNode(v), root
            return root
        # Insert nodes to d = 1 @ d == 2
        if d-1 == 1:
            if root.left:
                root.left, root.left.left = TreeNode(v), root.left
            else:
                root.left = TreeNode(v)
            if root.right:
                root.right, root.right.right = TreeNode(v), root.right
            else:
                root.right = TreeNode(v)
            return root
        # Not meet target depth, continue digging
        self.addOneRow(root.left, v, d-1)
        self.addOneRow(root.right, v, d-1)
        return root

    def levelOrderTraversal(self, root):
        if root is None:
            return []
        ans = []
        q = collections.deque()
        q.append(root)
        while q:
            curNode = q.popleft()
            ans.append(curNode.val)
            if curNode.left:
                q.append(curNode.left)
            if curNode.right:
                q.append(curNode.right)
        return ans

# Main
if __name__ == '__main__':
    n0 = TreeNode(4)
    n1 = TreeNode(2)
    n2 = TreeNode(3)
    n3 = TreeNode(1)
    n0.left = n1
    n1.left, n1.right = n2, n3

    newRoot = Solution().addOneRow(n0, 1, 3)
    print(Solution().levelOrderTraversal(newRoot))

    m0 = TreeNode(4)
    m1 = TreeNode(2)
    m2 = TreeNode(6)
    m3 = TreeNode(3)
    m4 = TreeNode(1)
    m5 = TreeNode(5)
    m0.left, m0.right = m1, m2
    m1.left, m1.right = m3, m4
    m2.left = m5
    newRoot = Solution().addOneRow(m0, 1, 2)
    print(Solution().levelOrderTraversal(newRoot))

    m0 = TreeNode(4)
    m1 = TreeNode(2)
    m2 = TreeNode(6)
    m3 = TreeNode(3)
    m4 = TreeNode(1)
    m5 = TreeNode(5)
    m0.left, m0.right = m1, m2
    m1.left, m1.right = m3, m4
    m2.left = m5
    newRoot = Solution().addOneRow(m0, 1, 1)
    print(Solution().levelOrderTraversal(newRoot))
