# 812. Largest Triangle Area

# Given an array of points on the X-Y plane points where points[i] = [xi, yi], return the area of the largest triangle that can be formed by any three different points. Answers within 10-5 of the actual answer will be accepted.

 

# Example 1:


# Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
# Output: 2.00000
# Explanation: The five points are shown in the above figure. The red triangle is the largest.
# Example 2:

# Input: points = [[1,0],[0,0],[0,1]]
# Output: 0.50000
 

# Constraints:

# 3 <= points.length <= 50
# -50 <= xi, yi <= 50
# All the given points are unique.

# Code: Python 3

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        # x1,x2,y1,y2 = 51,-51,51,-51
        # for index,value in enumerate(points): 
        #     x1 = min(x1,value[0])
        #     x2 = max(x2,value[0])
        #     y1 = min(y1,value[1])
        #     y2 = max(y2,value[1])  
        # return 0.5 * (x2-x1) * (y2-y1)
        
        def area(p1, p2, p3):
            return 0.5 * abs(
                p1[0]*(p2[1]-p3[1]) +
                p2[0]*(p3[1]-p1[1]) +
                p3[0]*(p1[1]-p2[1])
            )
        
        max_area = 0
        for p1, p2, p3 in combinations(points, 3):
            max_area = max(max_area, area(p1, p2, p3))
        return max_area
