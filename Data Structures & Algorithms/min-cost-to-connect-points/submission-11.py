class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        n = len(points)
        seen = set()
        total_cost = 0
        heap = [(0,0)]

        while len(seen) < n:
            dist, i = heapq.heappop(heap)

            if i in seen:
                continue
            
            seen.add(i)
            total_cost += dist
            xi, yi = points[i]

            for j in range(n):
                if j not in seen:
                    xj, yj = points[j]
                    nei_dist = abs(xi-xj) + abs(yi-yj)
                    heapq.heappush(heap, [nei_dist, j])
        
        return total_cost