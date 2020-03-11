# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        def sol(root) :
            sum = 0
            if root != None :
                if root.val >= L and root.val <= R :
                    sum += root.val
                return sol(root.left) + \
                       sol(root.right) + \
                       sum 
            else: return 0
        return sol(root)
        
