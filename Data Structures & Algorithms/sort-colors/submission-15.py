class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        cnt = [0, 0, 0]

        for num in nums:
            cnt[num] += 1
        
        r, w, b = cnt

        nums[:r] = [0]*r
        nums[r:r+w] = [1]*w
        nums[r+w:] = [2]*b