# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return
       
        if root.left and root.right:
            # print(left)
            # print(right)
            left = self.isValidBST(root.left)
            right = self.isValidBST(root.right)
            if not left or not right:
                return False
            if left[0] >= root.val or right[1] <= root.val:
                return False
           
            return [max(left[0],right[0],root.val),min(left[1],right[1],root.val)]
        elif root.left:
            left = self.isValidBST(root.left)
            if not left:
                return False
            if left[0] >= root.val:
                
                return False
            
            return [max(left[0],root.val),min(left[1],root.val)]
        elif root.right:
            right = self.isValidBST(root.right)
            if not right:
                return False
            if right[1] <= root.val:
                
                return False
            
            return [max(right[0],root.val),min(right[1],root.val)]
        else:
            return [root.val,root.val]
        
        
        