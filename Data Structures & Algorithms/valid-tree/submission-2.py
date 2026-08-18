class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {i:[] for i in range(n)} 

        for u , v in edges :
            graph[u].append(v) 
            graph[v].append(u) 
        visited = set() 
        def bfs(node) :
            queue = deque([(node , -1)]) 
            visited.add(node) 

            while queue :
                vertex , parent = queue.popleft() 

                for other_vertex in graph[vertex] : 
                    if other_vertex == parent :
                        continue 
                    
                    if other_vertex in visited :
                        return False 
                    visited.add(other_vertex) 
                    queue.append((other_vertex , vertex)) 
            return True 
        if not bfs(0)  :
            return False 
        return len(visited) == n 