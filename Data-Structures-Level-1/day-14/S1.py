# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def orderBST(node):
            if node.left == None and node.right == None:
                return [node.val]
            out = []
            if node.left != None:
                out += orderBST(node.left)
            out.append(node.val)
            if node.right != None:
                out += orderBST(node.right)
            return out

        h = orderBST(root)
        return h == sorted(h) and len(h) == len(set(h))


# Solution from @jainatishay072
# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         return self.helper(root, -10000000000000000, 10000000000000000)

#     def helper(self, root, minrange, maxrange):
#         if root is None:
#             return True
#         if root.val <= minrange or root.val > maxrange:
#             return False
#         isLeft = self.helper(root.left, minrange, root.val-1)
#         isRight = self.helper(root.right, root.val, maxrange)
#         return isLeft and isRight
