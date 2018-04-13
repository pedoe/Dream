##############################################
## Author: I-No Liao                        ##
## Date of update: 2018/04/11               ##
## Description: Leetcode #226               ##
##############################################

# Invert a binary tree.
# 
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# to
# 
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, TreeNode
    # @return TreeNode
    def invertTree(self, root):
        if root is None:
            return root
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
    
    # @param root, TreeNode
    # @return TreeNode
    def preorderTraversal(self, root, ans):
        if root is None:
            return ans
        ans.append(root.val)
        self.preorderTraversal(root.left, ans)
        self.preorderTraversal(root.right, ans)
        return ans

# Main
if __name__ == '__main__':
    n0 = TreeNode(4)
    n1 = TreeNode(2)
    n2 = TreeNode(7)
    n3 = TreeNode(1)
    n4 = TreeNode(3)
    n5 = TreeNode(6)
    n6 = TreeNode(9)
    n0.left, n0.right = n1, n2
    n1.left, n1.right = n3, n4
    n2.left, n2.right = n5, n6
     
    print(Solution().preorderTraversal(n0, []))
    newRoot = Solution().invertTree(n0)
    print(Solution().preorderTraversal(newRoot, []))
