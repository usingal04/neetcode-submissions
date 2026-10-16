class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        m = len(heights)
        n = len(heights[0])

        p_seen = set()
        p_que = deque()

        a_seen = set()
        a_que = deque()

        for i in range(m):
            p_seen.add((i, 0))
            p_que.append((i, 0))
        
        for j in range(1, n):
            p_seen.add((0, j))
            p_que.append((0, j))
        
        for i in range(m):
            a_seen.add((i, n-1))
            a_que.append((i, n-1))
        
        for j in range(n-1):
            a_seen.add((m-1, j))
            a_que.append((m-1, j))
        
        def get_coordinates(que, seen):
            while que:
                i, j = que.popleft()
                for i_off, j_off in [(0,1), (1,0), (0,-1),(-1,0)]:
                    r, c = i+i_off, j+j_off
                    if 0<=r<m and 0<=c<n and (r,c) not in seen and heights[r][c] >= heights[i][j]:
                        que.append((r, c))
                        seen.add((r, c))
        
        get_coordinates(a_que, a_seen)
        get_coordinates(p_que, p_seen)

        return list(a_seen.intersection(p_seen))