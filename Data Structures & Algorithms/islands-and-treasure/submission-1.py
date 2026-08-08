class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        direction = ((-1 , 0) , (1,0) , (0,-1) , (0,1)) 
        queue = deque([]) 
        visited = set() 
        for i in range(len(grid)) :
            for j in range(len(grid[0])) :
                if grid[i][j] == 0 :  
                    visited.add((i,j))
                    queue.append((i,j)) 
        
        val = 1 
        while queue :
            level = len(queue) 
            for i in range(level) : 
                r , c = queue.popleft() 
                
                for row , col in direction : 
                    new_row = r + row 
                    new_col = c + col 

                    if new_row < 0 or new_row >= len(grid) or new_col < 0 or new_col >= len(grid[0]) or (new_row,new_col) in visited or grid[new_row][new_col] == -1: 
                        continue   
                    grid[new_row][new_col] = val 
                    queue.append((new_row , new_col)) 
                    visited.add((new_row , new_col)) 
            val += 1 
