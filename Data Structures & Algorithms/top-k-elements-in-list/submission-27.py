class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        h = {}

        for num in nums:
            if num in h:
                h[num] += 1
            else:
                h[num] = 1
        
        heap = []

        for key, val in h.items():
            if len(heap) < k:
                heapq.heappush(heap, [val, key])
            else:
                heapq.heappushpop(heap, [val, key])
        
        return [node[1] for node in heap]