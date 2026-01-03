# 1411. Number of Ways to Paint N × 3 Grid

# [Hard]

# You have a grid of size n x 3 and you want to paint each cell of the grid with exactly one of the three colors: Red, Yellow, or Green while making sure that no two adjacent cells have the same color (i.e., no two cells that share vertical or horizontal sides have the same color).

# Given n the number of rows of the grid, return the number of ways you can paint this grid. As the answer may grow large, the answer must be computed modulo 109 + 7.

 

# Example 1:


# Input: n = 1
# Output: 12
# Explanation: There are 12 possible way to paint the grid as shown.
# Example 2:

# Input: n = 5000
# Output: 30228214
 

# Constraints:

# n == grid.length
# 1 <= n <= 5000

# Code: Python 3

class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 1000000007
        x, y = 6, 6
        
        for i in range(2, n + 1):
            new_x = (3 * x + 2 * y) % MOD
            new_y = (2 * x + 2 * y) % MOD
            x, y = new_x, new_y
        
        return (x + y) % MOD