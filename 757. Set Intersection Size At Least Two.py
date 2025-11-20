# 757. Set Intersection Size At Least Two

# [Hard]

# You are given a 2D integer array intervals where intervals[i] = [starti, endi] represents all the integers from starti to endi inclusively.

# A containing set is an array nums where each interval from intervals has at least two integers in nums.

# For example, if intervals = [[1,3], [3,7], [8,9]], then [1,2,4,7,8,9] and [2,3,4,8,9] are containing sets.
# Return the minimum possible size of a containing set.

 

# Example 1:

# Input: intervals = [[1,3],[3,7],[8,9]]
# Output: 5
# Explanation: let nums = [2, 3, 4, 8, 9].
# It can be shown that there cannot be any containing array of size 4.
# Example 2:

# Input: intervals = [[1,3],[1,4],[2,5],[3,5]]
# Output: 3
# Explanation: let nums = [2, 3, 4].
# It can be shown that there cannot be any containing array of size 2.
# Example 3:

# Input: intervals = [[1,2],[2,3],[2,4],[4,5]]
# Output: 5
# Explanation: let nums = [1, 2, 3, 4, 5].
# It can be shown that there cannot be any containing array of size 4.
 

# Constraints:

# 1 <= intervals.length <= 3000
# intervals[i].length == 2
# 0 <= starti < endi <= 108

# Code: Python 3

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))

        # the two largest selected numbers so far
        p1 = -1  
        p2 = -1
        ans = 0

        for s, e in intervals:
            # Case 1: both p1 and p2 are inside interval
            if s <= p1:
                continue

            # Case 2: only p2 is inside
            elif s <= p2:
                ans += 1
                p1 = p2
                p2 = e  # pick 1 new number: e

            # Case 3: none inside → need to add two numbers
            else:
                ans += 2
                p1 = e - 1
                p2 = e

        return ans
