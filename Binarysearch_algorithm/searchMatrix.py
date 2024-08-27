from typing import List

def search2DMatrix(matrix: List[List[int]], target: int) -> bool:
    n = len(matrix[0])
    m = len(matrix)
    left = 0
    right = (m * n) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_val = matrix[mid // n][mid % n]

        if target == mid_val:
            return True
        elif target < mid_val:
            right = mid - 1
        else:
            left = mid + 1

    return False

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
target = 15
result = search2DMatrix(matrix, target)
print(result)
