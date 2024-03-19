# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        build =[]
        sum_ = 0
        def dfs(node):
            nonlocal sum_,build
            if not node:                
                return
            build.append(str(node.val))
            left = dfs(node.left)
            right = dfs(node.right)
            if not left  and not right:
                sum_ += int("".join(build))
            build.pop()
            return True
        dfs(root)
        return sum_