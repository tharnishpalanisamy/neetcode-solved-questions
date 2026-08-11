class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i:[] for i in range(numCourses) }  

        for u , v in prerequisites :
            graph[v].append(u)  
        self.cycle = False 
        visited = set() 
        path = set()  
        def dfs(node , path) :  
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
        for node in graph :
            if node not in visited :
                dfs(node , path) 
        return not self.cycle 
