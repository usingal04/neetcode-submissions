class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        left_arr = [0]*n
        right_arr = [0]*n
        left_mult = 1
        right_mult = 1

        for i in range(n):
            j = -i-1
            left_arr[i] = left_mult
            right_arr[j] = right_mult
            left_mult *= nums[i]
            right_mult *= nums[j]
        
        return [l*r for l, r in zip(left_arr, right_arr)]