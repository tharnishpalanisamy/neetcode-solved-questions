class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        l , r = max(nums) , sum(nums) 
        res = r 

        def canSplit(largestnum) :
            subarr = 0 
            total = 0 
            for n in nums :
                total += n 
                if total > largestnum :
                    subarr += 1 
                    total = n 
            return subarr+1 <= k 

        while l <= r :
            mid = (l+r)//2 
            if canSplit(mid) :
                res = mid 
                r = mid - 1 
            else:
                l = mid + 1 
        return res