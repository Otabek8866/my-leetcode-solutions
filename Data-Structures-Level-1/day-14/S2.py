# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
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

        for i in range(len(h)-1):
            num = k - h[i]
            if num in h[i+1:]:
                return True
        return False

# solution from @kevin_thelly
# class Solution:
#     def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
#         dic = {}

#         def traverse(root):
#             if root is None:
#                 return False
#             if root.val not in dic:
#                 dic[k-root.val] = 1
#             else:
#                 return True
#             return traverse(root.left) or traverse(root.right)

#         return traverse(root)
