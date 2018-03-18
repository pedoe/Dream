##############################################
## Author: I-No Liao                        ##
## Date of update: 2018/03/09               ##
## Description: Leetcode #160               ##
##############################################

# Write a program to find the node at which the intersection of two singly linked lists begins.
# 
#
# For example, the following two linked lists:
#
# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3
#                    ↗            
# B:     b1 → b2 → b3
# begin to intersect at node c1.
#
#
# Notes:
#
# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
#########################################################################################
#        # Solution 1: O(n^2)
#        # Fail at Time Complexity requirement
#        curNode_A, curNode_B = headA, headB
#        while curNode_A != None:
#            while curNode_B != None:
#                if curNode_B.val == curNode_A.val:
#                    return curNode_B
#                else:
#                    curNode_B = curNode_B.next
#            curNode_A = curNode_A.next
#            curNode_B = headB
#        return None
#########################################################################################
#        # Solution 2: O(3n)
#        list_a = []
#        list_b = []
#        curNode_A, curNode_B = headA, headB
#        while curNode_A != None:
#            list_a.append(curNode_A.val)
#            curNode_A = curNode_A.next
#        while curNode_B != None:
#            list_b.append(curNode_B.val)
#            curNode_B = curNode_B.next
#
#        list_a.reverse()
#        list_b.reverse()
#
#        if len(list_a) > 0 and len(list_b) > 0:
#            i = 0
#            while list_a[i] == list_b[i]:
#                i += 1
#                if i >= min( len(list_a), len(list_b) ):
#                    break
#
#            intersect = len(list_a) - i + 1 # The intersection point
#            if intersect > len(list_a):
#                return None
#            else:
#                curNode_A = headA
#                for i in range(1, intersect, 1):
#                    curNode_A = curNode_A.next
#                return curNode_A
#        else:
#            return None
#########################################################################################
#        # Solution 3: O(3n)
#        # This is the same as Solution2 except tha lists now contain entire ListNode
#        # instead of only keys
#        list_a = []
#        list_b = []
#        curNode_A, curNode_B = headA, headB
#        while curNode_A != None:
#            list_a.append(curNode_A)
#            curNode_A = curNode_A.next
#        while curNode_B != None:
#            list_b.append(curNode_B)
#            curNode_B = curNode_B.next
#
#        list_a.reverse()
#        list_b.reverse()
#
#        if len(list_a) > 0 and len(list_b) > 0:
#            i = 0
#            while list_a[i] == list_b[i]:
#                i += 1
#                if i >= min( len(list_a), len(list_b) ):
#                    break
#            if i == 0:
#                return None
#            else:
#                return list_a[i-1]
#        else:
#            return None
#########################################################################################
        # Solution 4: O(m+n)
        # Courtesy of kamyu104 =)
        curNodeA, curNodeB = headA, headB
        tailA, tailB, intersectNode = None, None, None
        while curNodeA and curNodeB:
            if curNodeA == curNodeB:
                intersectNode = curNodeA
                break
            if curNodeA.next:
                curNodeA = curNodeA.next
            elif tailA == None:
                tailA, curNodeA = curNodeA, headB
            else:
                break

            if curNodeB.next:
                curNodeB = curNodeB.next
            elif tailB == None:
                tailB, curNodeB = curNodeB, headA
            else:
                break
        return intersectNode

#########################################################################################

# Main
if __name__ == '__main__':
    a1 = ListNode('a1')
    a2 = ListNode('a2')
    b1 = ListNode('b1')
    b2 = ListNode('b2')
    b3 = ListNode('b3')
    c1 = ListNode('c1')
    c2 = ListNode('c2')
    c3 = ListNode('c3')

    a1.next, a2.next = a2, c3
    b1.next, b2.next, b3.next = b2, b3, c1
    c1.next, c2.next, c3.next = c2, c3, None
    
    Sol = Solution()
    intersectNode = Sol.getIntersectionNode( a1, b1 )
    if intersectNode != None:
        print( intersectNode.val )
    else:
        print( intersectNode )

