class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res, sol = [], []

        def backtrack(i, cur):
            if cur == target:
                res.append(sol[:])
                return
            
            if i == len(nums) or cur > target:
                return 
            
            backtrack(i+1, cur)

            sol.append(nums[i])
            backtrack(i, cur + nums[i])
            sol.pop()

        backtrack(0,0)
        return res