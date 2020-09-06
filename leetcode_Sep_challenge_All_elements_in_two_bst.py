# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        def pre_order(root):
            if root == None:
                return []
            else:
                return pre_order(root.left) + [root.val] + pre_order(root.right) # Pre_order tranverse the bst into a sortes list
        l1 = pre_order(root1)
        l2 = pre_order(root2)
        len1 = len(l1)
        len2 = len(l2)
        i = j = 0
        max = 1e5+1
        l1.append(max)
        l2.append(max) # add a number our of bound which is greater than every element
        ans = []
        while i < len1 or j < len2:
            if l1[i] <= l2[j]:
                ans.append(l1[i])
                i += 1
            else:
                ans.append(l2[j])
                j += 1
        return ans

"""
Manual test cases:
[2,1,4]
[1,0,3]

[]
[]

[2,1]
[1,null, 8]

[]
[2,1,100000]

[2,1,100000]
[]

[3]
[4]

[0,-10000,10000, -100000, -1, 1, 100000]
[4,-8794,28903, -100000, -5784, 233, 100000]
"""