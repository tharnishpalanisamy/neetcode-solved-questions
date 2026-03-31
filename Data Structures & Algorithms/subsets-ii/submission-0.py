class Solution:
    def subsetsWithDup(self, nums):
        res = [] 
        count = [] 

        def backtrack(path,index) : 
            if Counter(path) not in count :
                count.append(Counter(path)) 
                res.append(path[:]) 
                
            for i in range(index,len(nums)) :
                path.append(nums[i]) 
                backtrack(path,i + 1 ) 
                path.pop() 
        backtrack([],0) 
        return res

