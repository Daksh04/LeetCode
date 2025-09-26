# 611. Valid Triangle Number

# Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

 

# Example 1:

# Input: nums = [2,2,3,4]
# Output: 3
# Explanation: Valid combinations are: 
# 2,3,4 (using the first 2)
# 2,3,4 (using the second 2)
# 2,2,3
# Example 2:

# Input: nums = [4,2,3,4]
# Output: 4
 

# Constraints:

# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 1000

# Code : Python 3

def triangleNumber(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0

        nums.sort()
        count = 0

        # k is index of largest side
        for k in range(n - 1, 1, -1):
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    # all indices from i..j-1 with j form valid triangles with k
                    count += (j - i)
                    j -= 1
                else:
                    i += 1
        return count