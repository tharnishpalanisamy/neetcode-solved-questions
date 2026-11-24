class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        def bisect(arr , n ) :
            l = 0 
            r = len(arr) 

            while l < r :
                m = (l+r) // 2 

                if n > arr[m] :
                    l = m + 1 
                elif n < arr[m] :
                    r = m 
                else :
                    return m 
            return l 

        n = len(nums) 
        tails = [] 

        for n in nums : 
            pos = bisect(tails , n )
            if pos == len(tails) :
                tails.append(n) 
                continue
            tails[pos] = n 
        return len(tails)
            