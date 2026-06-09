class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = [] 
        nums.sort()
        def backtrack(path,total , index) : 
            if total == target :
                res.append(path[:]) 
                return 
            if total > target :
                return 

            for i in range(index , len(nums)) :
                if i > index and nums[i] == nums[i-1] :
                    continue
                path.append(nums[i]) 
                backtrack(path,total+nums[i] , i+1) 
                path.pop() 
        backtrack([],0,0) 
        return res
