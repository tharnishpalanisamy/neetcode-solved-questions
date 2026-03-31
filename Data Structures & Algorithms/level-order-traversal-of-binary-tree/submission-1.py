# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root :
            return [] 
        res = [] 
        queue = deque([root]) 
        while queue : 
            levelsize = len(queue) 
            level = []   
            for i in range(levelsize) :
                val = queue.popleft()  
                if val.left :
                    queue.append(val.left) 
                if val.right :
                    queue.append(val.right)
                level.append(val.val) 
            res.append(level)
        return res
            

