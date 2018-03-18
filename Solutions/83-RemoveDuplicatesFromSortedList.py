# Time:  O(n)
# Space: O(1)

# Given a sorted linked list, delete all duplicates such that each element appear only once.
#
# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.
#

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        while cur:
            nxt = cur.next
            while nxt and nxt.val == cur.val:
                nxt = nxt.next
            cur.next = nxt
            cur = nxt
        return head


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(3)

    tmp = head
    while tmp:
        print(tmp.val)
        tmp = tmp.next
    print('\n')

    result = Solution().deleteDuplicates(head)
    while result:
        print(result.val)
        result = result.next
