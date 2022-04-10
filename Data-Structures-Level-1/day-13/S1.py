# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            return None
        if root.val == val:
            return root
        check = self.searchBST(root.left, val)
        if check:
            return check
        check = self.searchBST(root.right, val)
        if check:
            return check
        return None
