# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorder(self,node):
        if not node:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        self.res.append(node.val)


    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #left,right,root
        self.res =[]

        self.postorder(root)

        return self.res