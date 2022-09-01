class Solution:
    def maxProfit(self, prices):
        cheap = prices[0]
        res = 0
        
        for i in range (1, len(prices)):
            cheap = min(cheap, prices[i])
            res = max(res, prices[i] - cheap)
        
        return res
