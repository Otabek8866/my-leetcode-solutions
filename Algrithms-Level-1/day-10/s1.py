# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1

        node1 = list1
        node2 = list2

        if node1.val <= node2.val:
            head = node1
            node1 = node1.next
        else:
            head = node2
            node2 = node2.next

        tmp = head
        while node1 and node2:
            if node1.val <= node2.val:
                tmp.next = node1
                node1 = node1.next
            else:
                tmp.next = node2
                node2 = node2.next
            tmp = tmp.next

        if node1 != None:
            tmp.next = node1
        else:
            tmp.next = node2

        return head
