# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def recursive(node):
            if node.next == None:
                return [node]

            result = [node]
            result += recursive(node.next)
            return result

        final_list = recursive(head)
        return final_list[len(final_list)//2]
