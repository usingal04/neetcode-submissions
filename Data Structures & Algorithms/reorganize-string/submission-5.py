class Solution:
    def reorganizeString(self, s: str) -> str:
        
        count = Counter(s)
        maxHeap = [[-cnt, val] for val, cnt in count.items()]
        heapq.heapify(maxHeap)
        res = ''
        prev = None

        while prev or maxHeap:
            if not maxHeap:
                return ""
            
            cnt, val = heapq.heappop(maxHeap)
            res += val
            cnt += 1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None

            if cnt != 0:
                prev = [cnt, val]
        
        return res