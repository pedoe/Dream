##############################################
## Author: I-No Liao                        ##
## Date of update: 2018/03/27               ##
## Description: Leetcode #113               ##
##############################################

# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
# 
# For example:
# Given the below binary tree and sum = 22,
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# return
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]

import collections

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    
    def __init__(self):
        self.preorder = []

    # @param, TreeNode
    # @return, void
    def LevelOrderTraversal(self, root):
        queue = collections.deque()
        result = []
        # Level-order traversal
        # Push root into queue
        # Pop curNode out of queue and store its value into the result
        # Push curNode's children, if any, into queue
        # When queue is empty, the level-order traversal is done
        queue.append(root)
        while len(queue):
            curNode = queue.popleft()
            result.append(curNode.val)
            if curNode.left:
                queue.append(curNode.left)
            if curNode.right:
                queue.append(curNode.right)
        print(result)
    
    def PreorderTraversal(self, root):
        if root == None:
            return
        self.preorder.append(root.val)
        self.PreorderTraversal(root.left)
        self.PreorderTraversal(root.right)
        return self.preorder

    # @param root, TreeNode
    # @return, boolean
    def isLeaf(self, node):
        if node.left is None and node.right is None:
            return True
        else:
            return False
    
    # @param root, TreeNode
    # @param Sum, integer
    # @return, list[list[int]]
    def pathSum(self, root, Sum):
        return self.pathSumRecur([], [], root, Sum)
    
    # @param result and current, list
    # @param root, TreeNode
    # @param Sum, integer
    # @param return, list[list[int]]
    def pathSumRecur(self, result, current, root, Sum):
        if root is None:
            return result

        if root.val == Sum and self.isLeaf(root):
            result.append(current + [root.val])
            return result

        current.append(root.val)
        # Preorder traveral:
        self.pathSumRecur(result, current, root.left, Sum-root.val)
        self.pathSumRecur(result, current, root.right, Sum-root.val)
        # pop() to go back to predecessor
        current.pop()
        return result

# Main
if __name__ == '__main__':
    n0 = TreeNode(5)
    n1 = TreeNode(4)
    n2 = TreeNode(8)
    n3 = TreeNode(11)
    n4 = TreeNode(13)
    n5 = TreeNode(4)
    n6 = TreeNode(7)
    n7 = TreeNode(2)
    n8 = TreeNode(5)
    n9 = TreeNode(1)

    n0.left, n0.right = n1, n2
    n1.left = n3
    n2.left, n2.right = n4, n5
    n3.left, n3.right = n6, n7
    n5.left, n5.right = n8, n9
    
    print( Solution().PreorderTraversal(n0) )
    print(Solution().pathSum(n0, 22))
    print(Solution().pathSum(n0, 27))
    print(Solution().pathSum(n0, 26))
    print(Solution().pathSum(n0, 18))
    print(Solution().pathSum(n0, 9))
