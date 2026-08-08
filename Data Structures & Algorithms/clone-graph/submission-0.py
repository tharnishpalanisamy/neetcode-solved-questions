"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']: 
        if not node :
            return None 
        
        clones = {
            node:Node(node.val)
        } 

        queue = deque([node] ) 

        while queue : 

            vertex = queue.popleft () 

            for neigh in vertex.neighbors :
                if neigh not in clones :
                    clones[neigh] = Node(neigh.val) 
                    queue.append(neigh) 
                clones[vertex].neighbors.append(clones[neigh] ) 
        return clones[node]