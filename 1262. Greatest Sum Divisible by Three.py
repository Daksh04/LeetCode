# 1262. Greatest Sum Divisible by Three

# [Medium]

# Given an integer array nums, return the maximum possible sum of elements of the array such that it is divisible by three.

 

# Example 1:

# Input: nums = [3,6,5,1,8]
# Output: 18
# Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).
# Example 2:

# Input: nums = [4]
# Output: 0
# Explanation: Since 4 is not divisible by 3, do not pick any number.
# Example 3:

# Input: nums = [1,2,3,4,4]
# Output: 12
# Explanation: Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3).
 

# Constraints:

# 1 <= nums.length <= 4 * 104
# 1 <= nums[i] <= 104

# Code:  Python 3

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        total = sum(nums)
        
        r1 = sorted([x for x in nums if x % 3 == 1])
        r2 = sorted([x for x in nums if x % 3 == 2])
        
        if total % 3 == 0:
            return total
        
        if total % 3 == 1:
            option1 = r1[0] if r1 else float('inf')
            option2 = sum(r2[:2]) if len(r2) >= 2 else float('inf')
            return total - min(option1, option2)
        
        # total % 3 == 2
        option1 = r2[0] if r2 else float('inf')
        option2 = sum(r1[:2]) if len(r1) >= 2 else float('inf')
        return total - min(option1, option2)
