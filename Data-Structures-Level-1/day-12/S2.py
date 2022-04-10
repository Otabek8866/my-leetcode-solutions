# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        #         def cal(node, total, targetSum):
        #             if node == None:
        #                 if targetSum == total:
        #                     return True
        #                 else:
        #                     return False

        #             if targetSum <= total:
        #                 return False

        #             else:
        #                 total += node.val
        #                 if cal(node.left, total, targetSum):
        #                     return True
        #                 elif cal(node.right, total, targetSum):
        #                     return True
        #                 else:
        #                     return False

        #         return False if root==None else cal(root, 0, targetSum)

        #       Solution adopted from @kevin_thelly

        def target(self, root, targetSum):
            if(root != None):
                targetSum = targetSum-root.val
                if(root.left == None and root.right == None):
                    if(targetSum == 0):
                        return True
                    else:
                        return False
            else:
                return False

            return (target(self, root.left, targetSum) or target(self, root.right, targetSum))
        #### end of target ####

        return target(self, root, targetSum)
