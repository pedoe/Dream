# Time:  O(n)
# Space: O(h)

# Given a Binary Search Tree and a target number, return true if there exist
# two elements in the BST such that their sum is equal to the given target.
#
# Example 1:
# Input:
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
#
# Target = 9
# Output: True
#
# Example 2:
# Input:
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
#
# Target = 28
# Output: False

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        # latonn's
        path = []
        self.InOrderTraversal(root, path)
        for i in range(len(path)):
            if k - path[i] in path[i + 1:]:
                return True
        return False

    def InOrderTraversal(self, node, path):
        if node is None:
            return

        self.InOrderTraversal(node.left, path)
        path.append(node.val)
        self.InOrderTraversal(node.right, path)

        # kamyu's
        # class BSTIterator(object):
        #     def __init__(self, root, forward):
        #         self.__node = root
        #         self.__forward = forward
        #         self.__s = []
        #         self.__cur = None
        #         self.next()
        #
        #     def val(self):
        #         return self.__cur
        #
        #     def next(self):
        #         while self.__node or self.__s:
        #             if self.__node:
        #                 self.__s.append(self.__node)
        #                 self.__node = self.__node.left if self.__forward else self.__node.right
        #             else:
        #                 self.__node = self.__s.pop()
        #                 self.__cur = self.__node.val
        #                 self.__node = self.__node.right if self.__forward else self.__node.left
        #                 break
        #
        # if not root:
        #     return False
        # left, right = BSTIterator(root, True), BSTIterator(root, False)
        # while left.val() < right.val():
        #     if left.val() + right.val() == k:
        #         return True
        #     elif left.val() + right.val() < k:
        #         left.next()
        #     else:
        #         right.next()
        # return False


if __name__ == '__main__':
    root = TreeNode(5)
    root.left, root.right = TreeNode(3), TreeNode(6)
    root.left.left, root.left.right = TreeNode(2), TreeNode(4)
    root.right.right = TreeNode(7)
    target = 9
    print(Solution().findTarget(root, target))
