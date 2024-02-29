class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        cList = []
        for i in range(len(matrix)):
            cList += matrix[i]

        matrix = cList
        del cList

        while True:
            if len(matrix) == 1 and matrix[0] != target:
                return False
            
            sliced = len(matrix) // 2
            if target > matrix[sliced]:
                matrix = matrix[sliced:]
            elif target < matrix[sliced]:
                matrix = matrix[:sliced]
            elif target == matrix[sliced]:
                return True

        return False