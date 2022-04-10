# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        result = []
        if root.left != None:
            result += self.inorderTraversal(root.left)
        result.append(root.val)
        if root.right != None:
            result += self.inorderTraversal(root.right)
        return result
