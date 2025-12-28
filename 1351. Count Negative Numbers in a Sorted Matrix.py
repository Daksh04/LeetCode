# 1351. Count Negative Numbers in a Sorted Matrix

# [Easy]

# Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

 

# Example 1:

# Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Output: 8
# Explanation: There are 8 negatives number in the matrix.
# Example 2:

# Input: grid = [[3,2],[1,0]]
# Output: 0
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 100
# -100 <= grid[i][j] <= 100

# Code: Python 3

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        count_neg = 0
        itr = 0

        for i in range(r):
            for j in range(c-1-itr,-1,-1):
                if grid[i][j] < 0:
                    #print(count_neg)
                    count_neg += r - i
                    itr += 1
                else:
                    break

        return  count_neg