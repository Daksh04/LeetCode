# 3531. Count Covered Buildings

# [Medium]

# You are given a positive integer n, representing an n x n city. You are also given a 2D grid buildings, where buildings[i] = [x, y] denotes a unique building located at coordinates [x, y].

# A building is covered if there is at least one building in all four directions: left, right, above, and below.

# Return the number of covered buildings.

 

# Example 1:



# Input: n = 3, buildings = [[1,2],[2,2],[3,2],[2,1],[2,3]]

# Output: 1

# Explanation:

# Only building [2,2] is covered as it has at least one building:
# above ([1,2])
# below ([3,2])
# left ([2,1])
# right ([2,3])
# Thus, the count of covered buildings is 1.
# Example 2:



# Input: n = 3, buildings = [[1,1],[1,2],[2,1],[2,2]]

# Output: 0

# Explanation:

# No building has at least one building in all four directions.
# Example 3:



# Input: n = 5, buildings = [[1,3],[3,2],[3,3],[3,5],[5,3]]

# Output: 1

# Explanation:

# Only building [3,3] is covered as it has at least one building:
# above ([1,3])
# below ([5,3])
# left ([3,2])
# right ([3,5])
# Thus, the count of covered buildings is 1.
 

# Constraints:

# 2 <= n <= 105
# 1 <= buildings.length <= 105 
# buildings[i] = [x, y]
# 1 <= x, y <= n
# All coordinates of buildings are unique.

# Code: Python 3

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        from bisect import bisect_left

        row = {}
        col = {}

        # Group coordinates by row and column
        for x, y in buildings:
            row.setdefault(y, []).append(x)
            col.setdefault(x, []).append(y)

        # Sort each list
        for r in row.values():
            r.sort()
        for c in col.values():
            c.sort()

        covered = 0

        for x, y in buildings:
            r = row[y]
            c = col[x]

            # Find positions using binary search
            ir = bisect_left(r, x)
            ic = bisect_left(c, y)

            has_left = ir > 0
            has_right = ir + 1 < len(r)
            has_down = ic > 0
            has_up = ic + 1 < len(c)

            if has_left and has_right and has_up and has_down:
                covered += 1

        return covered
        