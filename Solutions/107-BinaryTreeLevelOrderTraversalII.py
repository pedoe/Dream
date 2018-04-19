# Time:  O(n)
# Space: O(n)

# Given a binary tree, return the bottom-up level order traversal of its
# nodes' values. (ie, from left to right, level by level from leaf to root).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# return its bottom-up level order traversal as:
#
# [
#   [15,7],
#   [9,20],
#   [3]
# ]

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # latonn's
        result, answer = {}, []
        self.LevelOrderTraverse(root, 0, result)
        reverseLen = len(result)
        while reverseLen > 0:
            answer.append(result[reverseLen-1])
            reverseLen -= 1
        return answer

    def LevelOrderTraverse(self, node, depth, result):
        if node is None:
            return
        result.setdefault(depth, [])
        result[depth].append(node.val)
        self.LevelOrderTraverse(node.left, depth + 1, result)
        self.LevelOrderTraverse(node.right, depth + 1, result)

        # kamyu's
        # if root is None:
        #     return []
        #
        # result, current = [], [root]
        # while current:
        #     next_level, vals = [], []
        #     for node in current:
        #         vals.append(node.val)
        #         if node.left:
        #             next_level.append(node.left)
        #         if node.right:
        #             next_level.append(node.right)
        #     current = next_level
        #     result.append(vals)
        #
        # print(result)
        # return result[::-1]


if __name__ == '__main__':
    root = TreeNode(3)
    root.left, root.right = TreeNode(9), TreeNode(20)
    root.right.left, root.right.right = TreeNode(15), TreeNode(7)
    print(Solution().levelOrderBottom(root))

