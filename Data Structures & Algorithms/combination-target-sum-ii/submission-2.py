class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort() 
        res = [] 

        def backtrack(index,path,total) :
            if total == target :
                res.append(path[:]) 
                return 
            if index >= len(nums) or target < total :
                return 
            
            for i in range(index,len(nums)) : 
                if i > index and nums[i] == nums[i-1] :
                    continue
                path.append(nums[i]) 
                backtrack(i+1,path,total+nums[i]) 
                path.pop()  
        backtrack(0,[],0) 
        return res
