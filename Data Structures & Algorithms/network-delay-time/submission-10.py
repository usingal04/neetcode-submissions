class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        d = defaultdict(list)

        for u, v, t in times:
            d[u].append([v, t])
        
        min_times = {}
        heap = [(0, k)]

        while heap:
            timektoi, i = heapq.heappop(heap)

            if i in min_times:
                continue
            
            min_times[i] = timektoi

            for nei, nei_time in d[i]:
                if nei not in min_times:
                    heapq.heappush(heap, [nei_time + timektoi, nei])
        
        if len(min_times) == n:
            return max(min_times.values())
        else:
            return -1