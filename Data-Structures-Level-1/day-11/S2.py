class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # code adopted from shruthiraptor
        def Mirrorring(tree1, tree2):
            if not tree1 and not tree2:
                return True
            if tree1 and tree2:
                if tree1.val == tree2.val:
                    return Mirrorring(tree1.left, tree2.right) and Mirrorring(tree1.right, tree2.left)
            return False
        return (Mirrorring(root, root))
