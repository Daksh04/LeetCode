# 3578. Count Partitions With Max-Min Difference at Most K

# [Medium]

# You are given an integer array nums and an integer k. Your task is to partition nums into one or more non-empty contiguous segments such that in each segment, the difference between its maximum and minimum elements is at most k.

# Return the total number of ways to partition nums under this condition.

# Since the answer may be too large, return it modulo 109 + 7.

 

# Example 1:

# Input: nums = [9,4,1,3,7], k = 4

# Output: 6

# Explanation:

# There are 6 valid partitions where the difference between the maximum and minimum elements in each segment is at most k = 4:

# [[9], [4], [1], [3], [7]]
# [[9], [4], [1], [3, 7]]
# [[9], [4], [1, 3], [7]]
# [[9], [4, 1], [3], [7]]
# [[9], [4, 1], [3, 7]]
# [[9], [4, 1, 3], [7]]
# Example 2:

# Input: nums = [3,3,4], k = 0

# Output: 2

# Explanation:

# There are 2 valid partitions that satisfy the given conditions:

# [[3], [3], [4]]
# [[3, 3], [4]]
 

# Constraints:

# 2 <= nums.length <= 5 * 104
# 1 <= nums[i] <= 109
# 0 <= k <= 109

# Code: Python 3

class Solution:
    def countPartitions(self, nums, k):
        MOD = 10**9 + 7
        n = len(nums)

        from collections import deque

        dp = [0] * (n + 1)
        pre = [0] * (n + 1)

        dp[0] = pre[0] = 1

        maxq = deque()
        minq = deque()

        l = 0
        for r in range(n):
            # push nums[r] into monotonic max deque
            while maxq and maxq[-1] < nums[r]:
                maxq.pop()
            maxq.append(nums[r])

            # push nums[r] into monotonic min deque
            while minq and minq[-1] > nums[r]:
                minq.pop()
            minq.append(nums[r])

            # shrink window until valid
            while maxq[0] - minq[0] > k:
                if maxq[0] == nums[l]:
                    maxq.popleft()
                if minq[0] == nums[l]:
                    minq.popleft()
                l += 1

            # dp[r+1] = sum(dp[l..r])
            dp[r + 1] = (pre[r] - (pre[l - 1] if l > 0 else 0)) % MOD

            # update prefix sum
            pre[r + 1] = (pre[r] + dp[r + 1]) % MOD

        return dp[n]
