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
        return self.sortedArrayToBSTRecu(nums, 0, len(nums))

    # latonn's
    def sortedArrayToBSTRecu(self, nums, start, end):
        if start == end:
            return None
        mid = int(start + (end - start)/2)
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBSTRecu(nums, start, mid)
        node.right = self.sortedArrayToBSTRecu(nums, mid + 1, end)
        return node

    # kamyu's
    # def sortedArrayToBSTRecu(self, nums, start, end):
    #     if start == end:
    #         return None
    #     mid = start + self.perfect_tree_pivot(end - start)
    #     node = TreeNode(nums[mid])
    #     node.left = self.sortedArrayToBSTRecu(nums, start, mid)
    #     node.right = self.sortedArrayToBSTRecu(nums, mid + 1, end)
    #     return node
    #
    # def perfect_tree_pivot(self, n):
    #     """
    #     Find the point to partition n keys for a perfect binary search tree
    #     """
    #     x = 1
    #     # find a power of 2 <= n//2
    #     # while x <= n//2:  # this loop could probably be written more elegantly :)
    #     #     x *= 2
    #     x = 1 << (n.bit_length() - 1)  # use the left bit shift, same as multiplying x by 2**n-1
    #
    #     if x // 2 - 1 <= (n - x):
    #         return x - 1  # case 1: the left subtree of the root is perfect and the right subtree has less nodes
    #     else:
    #         return n - x // 2  # case 2 == n - (x//2 - 1) - 1 : the left subtree of the root
    #         # has more nodes and the right subtree is perfect.


if __name__ == '__main__':
    nums = [-10, -3, 0, 5, 9, 11]
    root = Solution().sortedArrayToBST(nums)
    print(root.val)
    print(root.left.val)
    print(root.left.left.val)
    print(root.left.right.val)
    print(root.right.val)
    print(root.right.left.val)

