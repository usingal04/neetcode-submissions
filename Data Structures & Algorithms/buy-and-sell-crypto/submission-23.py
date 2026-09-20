class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minVal = float('inf')

        maxProf = 0

        for price in prices:
            if price < minVal:
                minVal = price
            
            profit = price - minVal
        
            if profit > maxProf:
                maxProf = profit
        
        return maxProf