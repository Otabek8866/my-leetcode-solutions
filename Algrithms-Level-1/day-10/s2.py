# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None

        node = head.next
        tail = head
        tail.next = None

        while node:
            tmp = node.next
            node.next = tail
            tail = node
            node = tmp

        return tail
