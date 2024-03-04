# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def tree(left,right):
            if left > right:
                return
            mid = (left+right)//2
            left = tree(left,mid-1)
            right = tree(mid+1,right)
            return TreeNode(nums[mid],left,right)
        return tree(0,len(nums)-1)