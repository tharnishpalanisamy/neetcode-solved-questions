# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root :
            return []
        res = [] 

        queue = deque([root]) 

        while queue :
            length = len(queue) 
            val = 0 
            for i in range(length) :
                val = queue.popleft()
                if val.left: 
                    queue.append(val.left) 
                if val.right:
                    queue.append(val.right) 
            if val :
                res.append(val.val) 
        return res
            