"""
Write an efficient algorithm that searches for a value "target" in an m x n integer matrix "matrix".
This matrix has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
ex:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
"""

class Solution1:    # O(n)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for line in matrix:
            if target in line:
                return True
        return False

class Solution2:     # O(logn)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        h = len(matrix)    # length
        w = len(matrix[0])  # width
        left = 0
        right = h * w -1
        """
        0 1 2 3
        4 5 6 7
        8 9 10 11       i = num // 4  j = num % 4
        """
        while left <= right:
            mid = (left + right) // 2
            i = mid // w
            j = mid % w
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                right = mid - 1
            else:
                left = mid + 1
        else:
            return False
