# Time:
# Space:

# Given an array where elements are sorted in ascending order,
# convert it to a height balanced BST.
#
# For this problem, a height-balanced binary tree is defined as
# a binary tree in which the depth of the two subtrees of every
# node never differ by more than 1.
#
# Example:
#
# Given the sorted array: [-10,-3,0,5,9],
#
# One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
#
#       0
#      / \
#    -3   9
#    /   /
#  -10  5

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        # def maxDepth(node):
        #     if not node:
        #         return 0
        #     left = maxDepth(node.left)
        #     right = maxDepth(node.right)
        #     return max(left, right) + 1
        #
        # def isBalanced(node):
        #     leftDepth = maxDepth(node.left)
        #     rightDepth = maxDepth(node.right)
        #     return True if abs(leftDepth - rightDepth) <= 1 else False
        #
        # def leftRotate(root):
        #     root, root.left = root.right, root
        #     return root
        #
        # def rightRotate(root):
        #     root, root.right = root.left, root
        #
        # root = TreeNode(nums[0])
        # print(root.val)
        # for i in range(1, len(nums)):
        #     tmp = root
        #     print(i, root.val)
        #     while tmp.right:
        #         tmp = tmp.right
        #     tmp.right = TreeNode(nums[i])
        #     if not isBalanced(root):
        #         root = leftRotate(root)
        #
        # return root

        return self.sortedArrayToBSTRecu(nums, 0, len(nums))

    def sortedArrayToBSTRecu(self, nums, start, end):
        if start == end:
            return None
        mid = start + self.perfect_tree_pivot(end - start)
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBSTRecu(nums, start, mid)
        node.right = self.sortedArrayToBSTRecu(nums, mid + 1, end)
        return node

    def perfect_tree_pivot(self, n):
        x = 1 << (n.bit_length() - 1)

        if x // 2 - 1 <= (n - x):
            return x - 1
        else:
            return n - x // 2


if __name__ == '__main__':
    nums = [-10, -3, 0, 5, 9]
    root = Solution().sortedArrayToBST(nums)
    print(root.val)
    print(root.left.val)
    print(root.left.left.val)
    print(root.left.right.val)
    print(root.right.val)
