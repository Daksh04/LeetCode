# 1523. Count Odd Numbers in an Interval Range

# [Easy]

# Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

 

# Example 1:

# Input: low = 3, high = 7
# Output: 3
# Explanation: The odd numbers between 3 and 7 are [3,5,7].
# Example 2:

# Input: low = 8, high = 10
# Output: 1
# Explanation: The odd numbers between 8 and 10 are [9].
 

# Constraints:

# 0 <= low <= high <= 10^9

# Code: Python 3

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        #More optimized
        return ((high + 1) // 2) - (low // 2)
        
        #If both low and high are odd
        if(low % 2 != 0 and high % 2 != 0):
            return 2 + ((high - low - 1) // 2)
        #If both low and high are even
        if(low % 2 == 0 and high % 2 == 0):
            return ((high - low - 1) // 2) + 1
        #If both low and high are even & odd
        else:
            return 1 + ((high - low - 1) // 2)
        