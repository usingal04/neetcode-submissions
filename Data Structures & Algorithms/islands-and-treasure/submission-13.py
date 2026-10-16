class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        m = len(grid)
        n = len(grid[0])
        q = deque()
        water = -1
        treasure = 0
        land = (2**31) - 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == treasure:
                    q.append((i, j, 0))
        
        while q:
            i, j, d = q.popleft()

            for i_off, j_off in [(0,1), (1,0), (0,-1), (-1,0)]:
                r, c = i+i_off, j+j_off
                if 0<=r<m and 0<=c<n and grid[r][c] == land:
                    grid[r][c] = d+1
                    q.append((r, c, d+1))
        