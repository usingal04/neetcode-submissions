class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        left_max_wall = [0]*n
        right_max_wall = [0]*n
        left_wall = 0
        right_wall = 0

        for i in range(n):
            j = -i-1
            left_max_wall[i] = left_wall
            right_max_wall[j] = right_wall
            left_wall = max(left_wall, height[i])
            right_wall = max(right_wall, height[j])
        
        summ = 0

        for i in range(n):
            pot = min(left_max_wall[i], right_max_wall[i])
            summ += max(0, pot - height[i])
        
        return summ
