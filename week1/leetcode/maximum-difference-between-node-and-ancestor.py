# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = []
        def traverse(root):
            if not root:
                return [float("inf"),-1]
            left = traverse(root.left)
            right = traverse(root.right)
            min_ = min(left[0],right[0])
            max_ = max(left[1],right[1])
            if min_ != float("inf") and max_ !=-1:
                ans.append(max(abs(root.val-max_),abs(root.val-min_)))
            elif min_ and min_ != float("inf"):
                ans.append(abs(root.val-min_))
            elif max_ !=-1:
                ans.append(abs(root.val-max_))
            return [min(root.val,min_),max(root.val,max_)]
        traverse(root)
        return max(ans)