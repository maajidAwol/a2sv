# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if not root:
            return
        if root == p or root ==q:
            return root
        
        
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if left == p and right == q or right == p and left ==q:
            return root
        if root == p and (left == q or right ==q):
            return root
        elif root == q and (left == p and right == p):
            return root

        return left or right