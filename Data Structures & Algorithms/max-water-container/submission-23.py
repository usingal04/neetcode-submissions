class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        maxCap = 0
        l, r = 0, len(heights)-1

        while l < r:
            minHeight = min(heights[l], heights[r])
            cap = minHeight * (r-l)
            maxCap = max(maxCap, cap)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxCap