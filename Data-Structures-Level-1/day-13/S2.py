# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def inserting(root, val):
            if root.val > val:
                if root.left != None:
                    inserting(root.left, val)
                else:
                    root.left = TreeNode(val)
            else:
                if root.right != None:
                    inserting(root.right, val)
                else:
                    root.right = TreeNode(val)

        if root == None:
            return TreeNode(val)
        else:
            inserting(root, val)
            return root
