class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        h = {}

        for num in nums:
            if num in h:
                h[num] += 1
            else:
                h[num] = 1
        
        for key, val in h.items():
            if val > len(nums) / 2:
                return key