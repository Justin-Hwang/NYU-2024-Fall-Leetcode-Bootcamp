class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Check if the first row and the first column have any zeroes
        first_row_has_zero = any(matrix[0][j] == 0 for j in range(len(matrix[0])))
        first_col_has_zero = any(matrix[i][0] == 0 for i in range(len(matrix)))
        
        # Use the first row and first column to mark rows and columns to be zeroed
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # Set zeroes for cells based on the markers in the first row and column
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # Handle the first row
        if first_row_has_zero:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        
        # Handle the first column
        if first_col_has_zero:
            for i in range(len(matrix)):
                matrix[i][0] = 0