# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # -------------- code adpoted from @TaiwanIndependence -----------------------
        def parser(root, lt, level=0):
            if not root:
                return lt
            if level == len(lt):
                lt.append([root.val])
            else:
                lt[level].append(root.val)
            parser(root.left, lt, level+1)
            parser(root.right, lt, level+1)
            return lt
        lt = list()
        return parser(root, lt)
