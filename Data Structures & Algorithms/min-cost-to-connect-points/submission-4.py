class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        self.parent = {} 
        self.size = {} 
        for i , j in points :
            self.parent[(i,j)] = (i,j) 
            self.size[(i,j)] = 1 
        
        graph = [] 
        n = len(points)      
        for i in range(n) : 
            for j in range(i+1 , n) :   
                x1 = points[i][0] 
                y1 = points[i][1] 
                x2 = points[j][0] 
                y2 = points[j][1] 

                distance = abs(x1 - x2) + abs(y1 - y2)  
                graph.append([distance , tuple(points[i]) , tuple(points[j]) ]) 
        graph.sort() 

        def find(x) :
            root = x 
            while root != self.parent[x]  :
                self.parent[x] , root = self.parent[self.parent[root]] , self.parent[root] 
            
            while self.parent[x] != x :
                self.parent[x] , x = root , self.parent[x] 
            return root 
        
        def union(a,b) :
            rootA = find(a) 
            rootB = find(b) 

            if rootA == rootB :
                return False  
            
            if self.size[rootA] < self.size[rootB] :
                rootA,rootB = rootB , rootA 
            self.size[rootA] += self.size[rootB] 
            self.parent[rootB] = rootA
            return True 

        mstWeight = 0 
        mstEdges = 0 
        for item in graph :  
            if union(item[1] , item[2]) :
                mstWeight += item[0]  
                if mstEdges == n-1 :
                    break 
                mstEdges += 1 

        return mstWeight
