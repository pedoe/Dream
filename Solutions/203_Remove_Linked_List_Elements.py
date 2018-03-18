##############################################
## Author: I-No Liao                        ##
## Date of update: 2018/03/09               ##
## Description: Leetcode #203               ##
##############################################

# Remove all elements from a linked list of integers that have value val.
#
# Example
# Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
# Return: 1 --> 2 --> 3 --> 4 --> 5

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        curNode = head
        preNode = ListNode(-1)
        preNode.next = curNode
        while curNode != None:
            if curNode.val == val:
                if curNode == head:
                    head = curNode.next
                tempNode = curNode
                preNode.next, curNode = curNode.next, curNode.next
                del( tempNode )
            else:
                preNode, curNode = curNode, curNode.next
        return head

# Main
if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(6)
    n4 = ListNode(3)
    n5 = ListNode(4)
    n6 = ListNode(5)
    n7 = ListNode(6)
    n1.next, n2.next, n3.next, n4.next, n5.next, n6.next, n7.next = n2, n3, n4, n5, n6, n7, None
    
    curNode = n1
    while curNode != None:
        print( curNode.val )
        curNode = curNode.next

    print()
    
    # Remove the target elements
    Sol = Solution()
    head = Sol.removeElements(n1, 6)

    curNode = head
    while curNode != None:
        print( curNode.val )
        curNode = curNode.next
