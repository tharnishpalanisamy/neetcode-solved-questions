class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = [] 
        
        def backtrack(path,total , index) : 
            if index > len(nums) :
                return
            if total == target :
                res.append(path[:]) 
                return
            if total > target :
                index += 1 
                return
            
            for i in range(index , len(nums) ) :
                path.append(nums[i]) 
                backtrack(path,total+nums[i] , i) 
                path.pop() 
        backtrack([], 0,0 ) 
        return res