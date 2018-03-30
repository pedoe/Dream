##############################################
## Author: I-No Liao                        ##
## Date of update: 2018/03/27               ##
## Description: Leetcode #437               ##
##############################################

# You are given a binary tree in which each node contains an integer value.
# 
# Find the number of paths that sum to a given value.
# 
# The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).
# 
# The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.
# 
# Example:
# 
# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
# 
#       10
#      /  \
#     5   -3
#    / \    \
#   3   2   11
#  / \   \
# 3  -2   1
# 
# Return 3. The paths that sum to 8 are:
# 
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3. -3 -> 11

import collections

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    
    def __init__(self):
        self.count = 0

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
    
    # @param root, TreeNode
    # @param Sum, Integer
    # @return, Integer
    # Time: O(n^2)
    def pathSum(self, root, Sum):
        if root is None:
            return 0
        
        count = 0
        q = collections.deque()
        q.append(root)
        while len(q) > 0:
            curNode = q.popleft()
            self.count = 0
            count += self.pathSumHelper(curNode, Sum)
            if curNode.left:
                q.append(curNode.left)
            if curNode.right:
                q.append(curNode.right)
        return count
    
    # @param root, TreeNode
    # @return, Integer
    # pathSumHelper counts # of sum from root to leaf.
    # Internal summation can not be computed due to Sum-root.val recursion.
    def pathSumHelper(self, root, Sum):
        if root is None:
            return self.count
        if root.val == Sum:
            self.count += 1

        self.pathSumHelper(root.left, Sum-root.val)
        self.pathSumHelper(root.right, Sum-root.val)
        return self.count
       
class kamyu104(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def pathSumHelper(root, curr, sum, lookup):
            if root is None:
                return 0
            
            # curr = path sum from root to the currently visited node
            curr += root.val
            
            # If curr-sum is in LUT, 
            result = lookup[curr-sum] if curr-sum in lookup else 0
            lookup[curr] += 1
            
            # Print the observation
            print("curr, result = %d, %d" %(curr, result))
            print(lookup)

            # result = result + left subtree + right subtree
            result += pathSumHelper(root.left, curr, sum, lookup) + \
                      pathSumHelper(root.right, curr, sum, lookup)
            
            # Current subtree has done visiting,
            # and been ready to return # of valid pathSum of current subtree.
            # Hence, subtract 1 from the dictionary and return. 
            lookup[curr] -= 1
            if lookup[curr] == 0:
                del lookup[curr]
            return result
        
        lookup = collections.defaultdict(int)
        lookup[0] = 1
        return pathSumHelper(root, 0, sum, lookup)

# Main
if __name__ == '__main__':
    n0 = TreeNode(10)
    n1 = TreeNode(5)
    n2 = TreeNode(-3)
    n3 = TreeNode(3)
    n4 = TreeNode(2)
    n5 = TreeNode(11)
    n6 = TreeNode(3)
    n7 = TreeNode(-2)
    n8 = TreeNode(1)

    n0.left, n0.right = n1, n2
    n1.left, n1.right = n3, n4
    n2.right = n5
    n3.left, n3.right = n6, n7
    n4.right = n8
    
    Solution().LevelOrderTraversal(n0)
    # print(Solution().pathSum(n0, 8))
    print(kamyu104().pathSum(n0, 8))
