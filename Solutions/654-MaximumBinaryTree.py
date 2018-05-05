# Time:  O(n)
# Space: O(n)

# Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:
#
# The root is the maximum number in the array.
# The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
# The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
# Construct the maximum tree by the given array and output the root node of this tree.
#
# Example 1:
# Input: [3,2,1,6,0,5]
# Output: return the tree root node representing the following tree:
#
#       6
#     /   \
#    3     5
#     \    /
#      2  0
#        \
#         1
# Note:
# The size of the given array will be in the range [1,1000].

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        # latonn's
        def constructMaxBTHelper(nums):
            if not nums:
                return

            maximum, position = nums[0], 0
            for i in range(1, len(nums)):
                if nums[i] > maximum:
                    maximum = nums[i]
                    position = i

            return TreeNode(maximum), position

        if not nums:
            return

        root, pos = constructMaxBTHelper(nums)
        root.left = self.constructMaximumBinaryTree(nums[:pos])
        root.right = self.constructMaximumBinaryTree(nums[pos+1:])

        return root

        # kamyu's
        # nodeStack = []
        # for num in nums:
        #     node = TreeNode(num)
        #     while nodeStack and num > nodeStack[-1].val:
        #         node.left = nodeStack.pop()
        #     if nodeStack:
        #         nodeStack[-1].right = node
        #     nodeStack.append(node)
        #     for i in nodeStack:
        #         print(i.val)
        # return nodeStack[0]


if __name__ == '__main__':
    input = [3, 2, 1, 6, 0, 5]
    root = Solution().constructMaximumBinaryTree(input)
    print('Answer:')
    print(root.val)
    print(root.left.val, root.right.val)
    print(root.left.right.val, root.right.left.val)
    print(root.left.right.right.val)