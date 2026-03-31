# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(r1,r2) :
            if not r1 and not r2 :
                return True 
            if not r1 or not r2 :
                return False
            if r1.val != r2.val :
                return False 
            return isSameTree(r1.left,r2.left) and isSameTree(r1.right,r2.right) 
        
        def dfs(root,subRoot) :
            if not root :
                return False 
            if isSameTree(root,subRoot) :
                return True 
            return dfs(root.left,subRoot) or dfs(root.right,subRoot)

        return dfs(root,subRoot)

 

        
            