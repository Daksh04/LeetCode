# 3510. Minimum Pair Removal to Sort Array II

# [Hard]

# Given an array nums, you can perform the following operation any number of times:

# Select the adjacent pair with the minimum sum in nums. If multiple such pairs exist, choose the leftmost one.
# Replace the pair with their sum.
# Return the minimum number of operations needed to make the array non-decreasing.

# An array is said to be non-decreasing if each element is greater than or equal to its previous element (if it exists).

 

# Example 1:

# Input: nums = [5,2,3,1]

# Output: 2

# Explanation:

# The pair (3,1) has the minimum sum of 4. After replacement, nums = [5,2,4].
# The pair (2,4) has the minimum sum of 6. After replacement, nums = [5,6].
# The array nums became non-decreasing in two operations.

# Example 2:

# Input: nums = [1,2,2]

# Output: 0

# Explanation:

# The array nums is already sorted.

 

# Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109

# Code: Python 3

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n=len(nums)
        # check if sorted
        if all(x<=y for x, y in pairwise(nums)):
            return 0
        rmv=[False]*n
        prv=[i-1 for i in range(n)]
        nxt=[i+1 if i+1<n else -1 for i in range(n)]

        heap=[(nums[i]+nums[i+1], i) for i in range(n-1)]
        heapq.heapify(heap)

        bad=sum( nums[i]>nums[i+1] for i in range(n-1))
        op=0
        while bad>0:
            Sum, i=heapq.heappop(heap)

            if rmv[i] or nxt[i]==-1: continue
            j=nxt[i]
            if rmv[j] or nums[i]+nums[j]!=Sum: continue

            pi=prv[i]
            nj=nxt[j]

            # remove old violations
            if pi!=-1 and nums[pi]>nums[i]: bad-=1
            if nums[i]>nums[j]: bad-=1
            if nj!=-1 and nums[j]>nums[nj]: bad-=1

            # merge
            nums[i]=Sum
            rmv[j]=True

            nxt[i]=nj
            if nj!=-1: prv[nj]=i
            
            # add new violations
            if pi!=-1 and nums[pi]>nums[i]: bad+=1
            if nj!=-1 and nums[i]>nums[nj]: bad+=1

            # update heap
            if pi!= -1:
                heapq.heappush(heap, (nums[pi]+nums[i], pi))
            if nj!= -1:
                heapq.heappush(heap, (nums[i]+nums[nj], i))
                
            op+=1
        return op
    