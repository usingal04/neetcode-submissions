class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        n = len(heights)
        maxArea = 0
        stk= []

        for i in range(n+1):
            while stk and (i == n or heights[stk[-1]] >= heights[i]):
                height = heights[stk.pop()]
                width = i if not stk else i - stk[-1] - 1
                maxArea = max(maxArea, height * width)
            stk.append(i)
        
        return maxArea