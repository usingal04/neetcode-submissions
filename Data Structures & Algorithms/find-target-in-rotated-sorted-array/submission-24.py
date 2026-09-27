class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums)-1

        while l < r:
            mid = l + (r-l) // 2
            if nums[mid] > nums[r]:
                l = mid+1
            else:
                r = mid
        
        min_index = l

        if min_index == 0:
            l, r = 0, len(nums)-1
        elif target >= nums[0] and target <= nums[min_index-1]:
            l, r = 0, min_index-1
        else:
            l, r = min_index, len(nums)-1
        
        while l <= r:
            mid = l + (r-l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid-1
            else:
                l = mid+1

        return -1