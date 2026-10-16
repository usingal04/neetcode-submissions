class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        q = deque()
        num_fresh = 0
        empty = 0
        fresh = 1
        rotten = 2

        for i in range(m):
            for j in range(n):
                if grid[i][j] == fresh:
                    num_fresh += 1
                if grid[i][j] == rotten:
                    q.append((i, j))
        
        if num_fresh == 0:
            return 0
        
        t = -1

        while q:
            t += 1

            for _ in range(len(q)):
                i, j = q.popleft()
                for i_off, j_off in [(0,1), (1,0), (0,-1), (-1,0)]:
                    r, c = i+i_off, j+j_off
                    if 0<=r<m and 0<=c<n and grid[r][c] == fresh:
                        grid[r][c] = rotten
                        num_fresh -= 1
                        q.append((r,c))
        
        if num_fresh == 0:
            return t
        else:
            return -1