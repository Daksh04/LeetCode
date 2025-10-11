# 3186. Maximum Total Damage With Spell Casting

# A magician has various spells.

# You are given an array power, where each element represents the damage of a spell. Multiple spells can have the same damage value.

# It is a known fact that if a magician decides to cast a spell with a damage of power[i], they cannot cast any spell with a damage of power[i] - 2, power[i] - 1, power[i] + 1, or power[i] + 2.

# Each spell can be cast only once.

# Return the maximum possible total damage that a magician can cast.

 

# Example 1:

# Input: power = [1,1,3,4]

# Output: 6

# Explanation:

# The maximum possible damage of 6 is produced by casting spells 0, 1, 3 with damage 1, 1, 4.

# Example 2:

# Input: power = [7,1,6,6]

# Output: 13

# Explanation:

# The maximum possible damage of 13 is produced by casting spells 1, 2, 3 with damage 1, 6, 6.

 

# Constraints:

# 1 <= power.length <= 105
# 1 <= power[i] <= 109

# Code: Python 3

from collections import Counter
from bisect import bisect_right
from functools import lru_cache

class Solution:
    def maximumTotalDamage(self, power: list[int]) -> int:
        cnt = Counter(power)
        vals = sorted(cnt.keys())
        m = len(vals)
        
        # Compute nextIdx: for each i, find smallest j > i with vals[j] > vals[i] + 2
        nextIdx = [0] * m
        for i, v in enumerate(vals):
            # bisect_right returns first index where value > v + 2
            j = bisect_right(vals, v + 2, lo=i+1)
            nextIdx[i] = j
        
        @lru_cache(None)
        def dfs(i: int) -> int:
            if i >= m:
                return 0
            # Option 1: skip
            skip = dfs(i + 1)
            # Option 2: take all of vals[i]
            take = vals[i] * cnt[vals[i]] + dfs(nextIdx[i])
            return max(skip, take)
        
        return dfs(0)