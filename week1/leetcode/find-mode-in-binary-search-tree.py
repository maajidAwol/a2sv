# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        counted = defaultdict(int)
        def count(node):
            if not node:
                return
            
            left = count(node.left)
            right = count(node.right)
            counted[node.val] +=1
        count(root)
        
        max_ =max(counted.values())
        return [x for x in counted if counted[x] == max_]
