# Time:  O(n)
# Space: O(1)

# Given a singly linked list, determine if it is a palindrome.
#
# Follow up:
# Could you do it in O(n) time and O(1) space?
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        reverse, parity = None, head
        # Reverse the first half part of the list.
        while parity and parity.next:
            parity = parity.next.next
            head.next, reverse, head = reverse, head, head.next

        # If the number of the nodes is odd,
        # set the head of the tail list to the next of the median node.
        tail = head.next if parity else head

        # Compare the reversed first half list with the second half list.
        # And restore the reversed first half list.
        is_palindrome = True
        while reverse:
            is_palindrome = is_palindrome and reverse.val == tail.val
            tail, reverse = tail.next, reverse.next

        return is_palindrome


if __name__ == '__main__':
    head = ListNode(1)
    second = ListNode(2)
    third = ListNode(3)
    # third_half = ListNode(6)
    forth = ListNode(4)
    Last = ListNode(1)

    head.next = second
    second.next = third
    # third.next = third_half
    third.next = forth
    forth.next = Last

    print(Solution().isPalindrome(head))


