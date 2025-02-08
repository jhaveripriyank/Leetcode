class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        rows,cols=len(matrix),len(matrix[0])
        left,right=0,rows*cols-1

        while left<=right:
            mid = (left+right)//2
            rows_i=mid//cols
            cols_i=mid%cols

            if matrix[rows_i][cols_i] == target:
                return True
            elif matrix[rows_i][cols_i] < target:
                left = mid +1
            else:
                right = mid-1
        return False

        