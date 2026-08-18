class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        graph = {i:[] for i in range(1, n +1)} 

        
        def bfs(node , target) : 
            visited = set() 
            queue = deque([node]) 
            visited.add(node)

            while queue :
                vertex  = queue.popleft()  
                if vertex == target :
                    return True 

                for other_node in graph[vertex] : 
                    if other_node not in visited :
                        visited.add(other_node) 
                        queue.append(other_node)  
            return False



        for u , v in edges :
            if bfs(u , v) :
                return [u,v] 
            graph[u].append(v) 
            graph[v].append(u) 
        return [] 



