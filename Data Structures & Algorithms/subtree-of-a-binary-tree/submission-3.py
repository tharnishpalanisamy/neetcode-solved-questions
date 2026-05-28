# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 

    def isSameTree(self,root1,root2) :
            if not root1 and not root2 :
                return True 
            
            if not root1 or not root2 :
                return False 

            if root1.val != root2.val :
                return False 
            
            return self.isSameTree(root1.left,root2.left) and self.isSameTree(root1.right,root2.right)


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.cur = root 
        self.res = False
        def dfs(root,subRoot) :
            if not root :
                return False 
            
            if root.val == subRoot.val :
                if self.isSameTree(root,subRoot):
                    self.res = True  
            cur = dfs(root.left,subRoot) 
            cur = dfs(root.right,subRoot)  
        dfs(self.cur,subRoot)
        return self.res








