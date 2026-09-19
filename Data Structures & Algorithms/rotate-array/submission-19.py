class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        k = k % len(nums)
        r = len(nums) - k
        new = nums[:r]
        nums[:r] = []
        nums.extend(new)