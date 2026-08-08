class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set() 

        direction = ((-1,0) , (1,0) , (0,-1) , (0,1)) 
        self.res = 0 
        def bfs(i , j) :

            queue = deque([(i,j)] )  # 0 ,0 
            visited.add((i,j)) 
            val = 1
            while queue :

                r,c = queue.popleft()  

                for row, col in direction : 
                    new_row = r + row 
                    new_col = c + col 

                    if new_row < 0 or new_row >= len(grid) or new_col < 0 or new_col >= len(grid[0]) or grid[new_row][new_col] == 0 or (new_row,new_col) in visited: 
                        continue  
                    val += 1 
                    visited.add((new_row , new_col)) 
                    queue.append((new_row,new_col)) 
            self.res = max(val , self.res) 
        
        for i in range(len(grid)) :
            for j in range(len(grid[0]) ) :
                if grid[i][j] == 1 and (i,j) not in visited :
                    bfs(i,j) 
        return self.res


                    
 

            
