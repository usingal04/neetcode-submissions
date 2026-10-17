class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        m = len(matrix)
        n = len(matrix[0])
        left_wall = -1
        top_wall = 0
        right_wall = n
        bottom_wall = m

        left, right, up, down = 0, 1, 2, 3
        res = []
        i, j = 0, 0
        direction = right

        while len(res) != m*n:
            if direction == right:
                while j < right_wall:
                    res.append(matrix[i][j])
                    j += 1
                right_wall -= 1
                i, j = i+1, j-1
                direction = down
            elif direction == down:
                while i < bottom_wall:
                    res.append(matrix[i][j])
                    i += 1
                bottom_wall -= 1
                i, j = i-1, j-1
                direction = left
            elif direction == left:
                while j > left_wall:
                    res.append(matrix[i][j])
                    j -= 1
                left_wall += 1
                i, j = i-1, j+1
                direction = up
            else:
                while i > top_wall:
                    res.append(matrix[i][j])
                    i -= 1
                top_wall += 1
                i, j = i+1, j+1
                direction = right
        
        return res