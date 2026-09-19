class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        h = {}
        res = []

        for num in nums:
            if num in h:
                h[num] += 1
            else:
                h[num] = 1
            
        for i in range(min(h.keys()), max(h.keys()) + 1):
            if i not in h:
                continue
            else:
                index = h[i]
                while index > 0:
                    res.append(i)
                    index -= 1
                
        return res