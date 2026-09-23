class Solution:
    def mySqrt(self, x: int) -> int:
        
        l, r = 1, x
        res = 0

        while l <= r:
            mid = l + (r-l) // 2
            sq = mid ** 2
            if sq == x:
                res = mid
                return res
            elif sq > x:
                r = mid-1
            else:
                l = mid+1
                res = mid
        
        return res