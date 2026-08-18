class Solution:
    def findOrder(self, n: int, pre: List[List[int]]) -> List[int]: 
        graph = {i:[] for i in range(n)} 

        for u , v in pre :
            graph[v].append(u) 
        visited = set() 
        self.cycle = False
        stack = [] 
        
        def dfs(node , path  ) : 
            if self.cycle :
                return 
            visited.add(node) 
            path.add(node)
            for other_node in graph[node] : 
                if other_node in path :
                    self.cycle = True 
                    return
                if other_node not in visited :  
    
                    dfs(other_node , path)  
            path.remove(node)
            stack.append(node) 

        for node in graph :
            if node not in visited : 
                path = set() 
                dfs(node , path) 

        return stack[::-1] if len(stack) == n else [] 