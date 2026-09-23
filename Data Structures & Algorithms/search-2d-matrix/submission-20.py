class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])
        t = m*n

        l, r = 0, t-1

        while l <= r:
            mid = l + (r-l) // 2
            midi = mid // n
            midj = mid % n

            if matrix[midi][midj] == target:
                return True
            elif matrix[midi][midj] > target:
                r = mid-1
            else:
                l = mid+1
        
        return False