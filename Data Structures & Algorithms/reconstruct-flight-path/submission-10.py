class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        d = defaultdict(list)

        for src, dst in tickets:
            heapq.heappush(d[src], dst)
        
        res = []
        
        def visit(airport):
            while d[airport]:
                next_airport = heapq.heappop(d[airport])
                visit(next_airport)
            res.append(airport)
        
        visit('JFK')
        return res[::-1]