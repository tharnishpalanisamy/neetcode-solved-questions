class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited = set() 
        direction = ( (-1 , 0) , (1,0) , (0,1) , (0,-1)) 
        def bfs(i,j) :
            queue = deque([(i,j)]) 

            while queue :  
                r , c = queue.popleft()  

                for row , col in direction : 
                    new_row = r + row 
                    new_col = c + col 

                    if new_row < 0 or new_row >= len(grid)  or new_col < 0 or new_col >= len(grid[0]) or (new_row ,new_col) in  visited or grid[new_row][new_col] == '0': 
                        continue   
                    
                    queue.append((new_row , new_col)) 
                    visited.add((new_row , new_col)) 

        islands = 0 

        for i in range(len(grid)) :
            for j in range(len(grid[0])) :
                if (i,j) not in visited and grid[i][j] == '1' :
                    bfs(i,j) 
                    islands += 1 
        return islands


