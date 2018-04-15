# Time:  O(n * h)
# Space: O(h)

# Given a binary tree, return all root-to-leaf paths.
#
# For example, given the following binary tree:
#
#    1
#  /   \
# 2     3
#  \
#   5
#
# All root-to-leaf paths are:
#
# ["1->2->5", "1->3"]

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        # latonn's
        def dfs(root, path):
            if root.left is None and root.right is None:
                self.ans.append(path)
            if root.left:
                dfs(root.left, path + "->" + str(root.left.val))
            if root.right:
                dfs(root.right, path + "->" + str(root.right.val))

        self.ans = []
        if root is None:
            return self.ans
        dfs(root, str(root.val))
        return self.ans

        # kamyu's
    #     path, ans = [], []
    #     self.binaryTreePathsHelper(root, path, ans)
    #     return ans
    #
    # def binaryTreePathsHelper(self, node, path, ans):
    #     if node is None:
    #         return
    #
    #     if node.left is None and node.right is None:
    #         pathStr = ""
    #         for n in path:
    #             pathStr += str(n) + '->'
    #         pathStr += str(node.val)
    #         ans.append(pathStr)
    #
    #     if node.left:
    #         path.append(node.val)
    #         self.binaryTreePathsHelper(node.left, path, ans)
    #         path.pop()
    #
    #     if node.right:
    #         path.append(node.val)
    #         self.binaryTreePathsHelper(node.right, path, ans)
    #         path.pop()


if __name__ == '__main__':
    root = TreeNode(1)
    root.left, root.right = TreeNode(2), TreeNode(4)
    root.left.right = TreeNode(3)

    print(Solution().binaryTreePaths(root))



