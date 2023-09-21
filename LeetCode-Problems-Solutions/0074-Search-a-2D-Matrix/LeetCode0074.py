""" LeetCode Problems: #74. Search a 2D Matrix

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1: Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3              Output: true
Example 2: Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13             Output: false """

def searchMatrix(matrix, target):
    m, n = len(matrix), len(matrix[0])
    
    find_row = False
    top_row, bottom_row = 0, m-1
    while (top_row <= bottom_row):
        middle_row = (top_row + bottom_row) // 2
        if (target >= matrix[middle_row][0] and target <= matrix[middle_row][n-1]):
            find_row = True
            row = middle_row
            break
        elif (target > matrix[middle_row][n-1]):
            top_row = middle_row + 1
        else:
            bottom_row = middle_row - 1
    if not find_row:
        return False
    
    left_column, right_column = 0, n-1
    while (left_column <= right_column):
        middle_column = (left_column + right_column) // 2
        if (target == matrix[row][middle_column]):
            return True
        elif (target > matrix[row][middle_column]):
            left_column = middle_column + 1
        else:
            right_column = middle_column - 1
    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(searchMatrix(matrix,target))