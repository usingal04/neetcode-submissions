class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = Counter(tasks)
        maxHeap = [-val for val in count.values()]
        heapq.heapify(maxHeap)
        q = deque()
        t = 0

        while q or maxHeap:
            t += 1

            if not maxHeap:
                t = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, t + n])
            
            if q and q[0][1] == t:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return t