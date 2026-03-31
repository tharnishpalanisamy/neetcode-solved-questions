class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [] 
        for i in range(len(nums)) :#[0,0]
            prd = 1
            for j in range(len(nums)):
                if j != i:
                    prd *= nums[j]
            output.append(prd)
        return output
