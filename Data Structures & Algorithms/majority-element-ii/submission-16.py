class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        h = {}

        for num in nums:
            if num in h:
                h[num] += 1
            else:
                h[num] = 1
        
        res = []

        for key, val in h.items():
            if val > len(nums) / 3:
                res.append(key)
        
        return res