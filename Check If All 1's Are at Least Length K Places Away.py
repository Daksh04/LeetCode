# 1437. Check If All 1's Are at Least Length K Places Away

# Given an binary array nums and an integer k, return true if all 1's are at least k places away from each other, otherwise return false.

 

# Example 1:


# Input: nums = [1,0,0,0,1,0,0,1], k = 2
# Output: true
# Explanation: Each of the 1s are at least 2 places away from each other.
# Example 2:


# Input: nums = [1,0,0,1,0,1], k = 2
# Output: false
# Explanation: The second 1 and third 1 are only one apart from each other.
 

# Constraints:

# 1 <= nums.length <= 105
# 0 <= k <= nums.length
# nums[i] is 0 or 1

# Code: Python 3

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        count=0
        start_1=False
        for i in range(0,len(nums),1):
            #print(i, nums[i],count)
            if nums[i] == 1:
                if(count<k and i!=0 and start_1==True):
                    return False
                count=0
                start_1=True #ignore first time 1
            else: #0
                if start_1==True:
                    count+=1
        return True
