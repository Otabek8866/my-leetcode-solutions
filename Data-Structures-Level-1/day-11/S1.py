# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def recursive(node, num):
            if node == None:
                return [0]
            if node.left == None and node.right == None:
                return [num]
            num += 1
            result = []
            if node.left != None:
                result += recursive(node.left, num)
            if node.right != None:
                result += recursive(node.right, num)
            return result

        depth_list = recursive(root, 1)
        return max(depth_list)
