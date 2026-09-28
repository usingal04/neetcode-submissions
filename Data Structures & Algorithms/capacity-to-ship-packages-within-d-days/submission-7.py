class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def d_works(d):
            day = 1
            total = 0

            for w in weights:
                if total + w > d:
                    total = 0
                    day += 1
                
                total += w
            
            return day <= days
        
        l, r = max(weights), sum(weights)

        while l < r:
            mid = l + (r-l) // 2
            if d_works(mid):
                r = mid
            else:
                l = mid+1
        
        return l