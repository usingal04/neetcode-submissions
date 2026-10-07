class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []

        for point in points:
            dist = point[0]**2 + point[1]**2
            if len(heap) < k:
                heapq.heappush(heap, [-dist, point])
            else:
                heapq.heappushpop(heap, [-dist, point])
            
        return [node[1] for node in heap]