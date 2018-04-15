# Time:  O(n)
# Space: O(h), h is height of binary tree

# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest
# path from the root node down to the nearest leaf node.

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # latonn's
        def depthHelper(node, minimum):
            if not node.left and not node.right:
                return 1

            if node.left and not node.right:
                depthLeft = depthHelper(node.left, minimum)
                return min(minimum, depthLeft) + 1
            elif node.right and not node.left:
                depthRight = depthHelper(node.right, minimum)
                return min(minimum, depthRight) + 1
            else:
                depthLeft = depthHelper(node.left, minimum)
                depthRight = depthHelper(node.right, minimum)
                return min(minimum, depthLeft, depthRight)+ 1

        if not root:
            return 0
        return depthHelper(root, float("inf"))

        # kamyu's
        # if root is None:
        #     return 0
        #
        # if root.left and root.right:
        #     return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        # else:
        #     return max(self.minDepth(root.left), self.minDepth(root.right)) + 1


if __name__ == '__main__':
    root, root.left, root.right = TreeNode(3), TreeNode(9), TreeNode(20)
    root.right.left, root.right.right = TreeNode(15), TreeNode(7)
    print('answer: ', Solution().minDepth(root))
