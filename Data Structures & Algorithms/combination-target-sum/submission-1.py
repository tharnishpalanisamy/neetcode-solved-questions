class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = [] 

        def backtrack(index,path,total): 
            if total == target :
                res.append(path[:])
                return 
            elif total > target :
                return 
            if index >= len(nums) :
                return 
            for i in range(index,len(nums)) :
                path.append(nums[i]) 
                backtrack(i,path,total + nums[i]) 
                path.pop() 
        backtrack(0,[],0) 
        return res
            