class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque([]) 

        directions = ((-1,0) , (1,0) , (0,-1) , (0,1)) 
        fresh = 0 
        for i in range(len(grid)) :
            for j in range(len(grid[0])) :
                if grid[i][j] == 2 : 
                    queue.append((i,j))  
                elif grid[i][j] == 1 :
                    fresh += 1 
        val = 0
        while queue :  
            level = len(queue)
            thisLevel = 0 
            for i in range(level) :
                r , c = queue.popleft() 

                for row , col in directions : 
                    new_row = row + r 
                    new_col = col + c 

                    if new_row < 0 or new_row >= len(grid) or new_col < 0 or new_col >= len(grid[0]) or grid[new_row][new_col] != 1 :
                        continue 
                    fresh -= 1 
                    thisLevel = 1 
                    grid[new_row][new_col] = 2 
                    queue.append((new_row , new_col) )
            val += thisLevel
        return val if fresh == 0 else -1