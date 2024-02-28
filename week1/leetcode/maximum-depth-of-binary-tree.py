# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        print(root)
        def depth(curr):
            if curr == None:
                return 0
            
            return max(1+depth(curr.left),1+depth(curr.right))
        return depth(root)