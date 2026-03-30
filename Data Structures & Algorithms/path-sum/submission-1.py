# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(root,currsum):
            if not root:
                return False

            currsum=currsum+root.val
            if not root.left and not root.right:
                return  currsum == targetSum
        
            left = dfs(root.left,currsum) 
            right = dfs(root.right,currsum)

            if left or right:
                return True
            else:
                return False    

        res=dfs(root,0)
        return res                   
        