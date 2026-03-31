class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0 
        minp = prices[0]
        for price in prices :
            minp = min(minp,price)
            profit = price-minp 
            res = max(res,profit)
        return res
        
