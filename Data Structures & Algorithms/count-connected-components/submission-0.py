class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set() 

        graph = {i:[] for i in range(n)} 

        for u , v in edges :
            graph[u].append(v) 
            graph[v].append(u) 

        def bfs(node) :
            queue = deque([node]) 
            visited.add(node) 

            while queue :
                vertex = queue.popleft() 

                for other_node in graph[vertex] : 
                    if other_node not in visited :
                        visited.add(other_node) 
                        queue.append(other_node) 
        res = 0 
        for node in graph :
            if node not in visited :
                bfs(node) 
                res += 1 

        return res