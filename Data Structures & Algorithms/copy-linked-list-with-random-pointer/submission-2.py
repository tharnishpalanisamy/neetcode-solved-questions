"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old = {None:None}  
        cur = head
        while cur :
            new_node = Node(cur.val)
            old[cur] = new_node
            cur = cur.next 
        
        cur = head  

        while cur :
            new_node = old[cur] 
            new_node.next = old[cur.next] 
            new_node.random = old[cur.random] 
            cur = cur.next 
        
        return old[head]