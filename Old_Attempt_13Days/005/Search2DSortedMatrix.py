class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False
        m, n = len(matrix), len(matrix[0])
        if n == 0:
            return False
        x, y = 0, n-1
        while True:
            if target > matrix[x][y]:
                x += 1
            elif target < matrix[x][y]:
                y -= 1
            elif target == matrix[x][y]:
                return True
            if x == m or y == -1:
                return False 
