# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        count = 0
        pos = defaultdict(list)
        def traverse(node):
            nonlocal count
            if not node:
                return
            if count %2 ==0:

                pos[count].append(node.val)
            else:
                pos[count] = [node.val] +pos[count]
            count +=1
            left = traverse(node.left)
            right = traverse(node.right)
            count -=1
        traverse(root)
        
        return pos.values()