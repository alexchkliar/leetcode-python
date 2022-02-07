# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        dummy = ListNode()
        tail = dummy
        dict = {}

        while head:
            if head.val not in dict:
                dict[head.val] = 1
                tail.next = head
            tail = tail.next
            head = head.next
        return dummy.next
