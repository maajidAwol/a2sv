# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def pre(curr,dir):
            if curr == None:
                return [-1]
            val = [curr.val]
            left = pre(curr.left,-1)
            right = pre(curr.right,1)
            if dir ==1:
                return val + left +right
            else:
                return  val + right+left

        return  pre(root.left,-1) == pre(root.right,1)