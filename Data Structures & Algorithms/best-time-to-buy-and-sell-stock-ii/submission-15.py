class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProf = 0

        for i in range(1, len(prices)):
            profit = prices[i] - prices[i-1]
            if profit > 0:
                maxProf += prices[i] - prices[i-1]
        
        return maxProf