##############################################
## Author: I-No Liao                        ##
## Date of update: 2018/03/26               ##
## Description: Leetcode #112               ##
##############################################

# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
# 
# For example:
# Given the below binary tree and sum = 22,
# 
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \      \
#         7    2      1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

import collections

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    
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
    
    # @param, TreeNode
    # @return, boolean
    def isLeaf(self, node):
        if node.left is None and node.right is None:
            return True
        else:
            return False
    
    # @param root,  TreeNode
    # @param Sum, integer
    # @return, boolean
    # Idea:
    # Traversal is basded on level-order traversal, so a queue is used.
    # To check the path sum, compute curNode.val - child.val during traversal.
    # When child.val is 0, check if child is leaf.
    # If yes, return true
    # if no, push child into queue and keep traversing until leaf is encountered
    def hasPathSum(self, root, Sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        elif Sum - root.val == 0 and self.isLeaf(root): 
            return True
        else:
            root.val = Sum - root.val
        
        queue = collections.deque()
        queue.append(root)
       
        while len(queue):
            curNode = queue.popleft()
            if curNode.left:
                if curNode.val - curNode.left.val == 0 and self.isLeaf(curNode.left):
                    return True
                else:
                    curNode.left.val = curNode.val - curNode.left.val
                    queue.append(curNode.left)
            if curNode.right:
                if curNode.val - curNode.right.val == 0 and self.isLeaf(curNode.right):
                    return True
                else:
                    curNode.right.val = curNode.val - curNode.right.val
                    queue.append(curNode.right)
        return False

class Kamyu104(object):
    # @param root, TreeNode
    # @param Sum, integer
    # @return, boolean
    # Idea:
    # Recursion
    def hasPathSum(self, root, Sum):
        if root is None:
            return False
        elif root.val == Sum and root.left is None and root.right is None:
            return True
        else:
            return self.hasPathSum(root.left, Sum-root.val) or self.hasPathSum(root.right, Sum-root.val)

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
    n8 = TreeNode(1)

    n0.left, n0.right = n1, n2
    n1.left = n3
    n2.left, n2.right = n4, n5
    n3.left, n3.right = n6, n7
    n5.right = n8
    
    Solution().LevelOrderTraversal(n0)
    # print(Solution().hasPathSum(n0, 22))
    # print(Solution().hasPathSum(n0, 27))
    # print(Solution().hasPathSum(n0, 26))
    # print(Solution().hasPathSum(n0, 18))
    # print(Solution().hasPathSum(n0, 9))

    print(Kamyu104().hasPathSum(n0, 22))
