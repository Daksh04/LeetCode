# 3003. Maximize the Number of Partitions After Operations

# You are given a string s and an integer k.

# First, you are allowed to change at most one index in s to another lowercase English letter.

# After that, do the following partitioning operation until s is empty:

# Choose the longest prefix of s containing at most k distinct characters.
# Delete the prefix from s and increase the number of partitions by one. The remaining characters (if any) in s maintain their initial order.
# Return an integer denoting the maximum number of resulting partitions after the operations by optimally choosing at most one index to change.

 

# Example 1:

# Input: s = "accca", k = 2

# Output: 3

# Explanation:

# The optimal way is to change s[2] to something other than a and c, for example, b. then it becomes "acbca".

# Then we perform the operations:

# The longest prefix containing at most 2 distinct characters is "ac", we remove it and s becomes "bca".
# Now The longest prefix containing at most 2 distinct characters is "bc", so we remove it and s becomes "a".
# Finally, we remove "a" and s becomes empty, so the procedure ends.
# Doing the operations, the string is divided into 3 partitions, so the answer is 3.

# Example 2:

# Input: s = "aabaab", k = 3

# Output: 1

# Explanation:

# Initially s contains 2 distinct characters, so whichever character we change, it will contain at most 3 distinct characters, so the longest prefix with at most 3 distinct characters would always be all of it, therefore the answer is 1.

# Example 3:

# Input: s = "xxyz", k = 1

# Output: 4

# Explanation:

# The optimal way is to change s[0] or s[1] to something other than characters in s, for example, to change s[0] to w.

# Then s becomes "wxyz", which consists of 4 distinct characters, so as k is 1, it will divide into 4 partitions.

 

# Constraints:

# 1 <= s.length <= 104
# s consists only of lowercase English letters.
# 1 <= k <= 26

# Code: Python 3

class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        n = len(s)
        
        @cache
        def dfs(i: int, mask: int, can_change: int) -> int:
            # If we've consumed the entire string, count the last partition
            if i >= n:
                return 1
            
            # Bit for the current character
            bit = 1 << (ord(s[i]) - ord('a'))
            new_mask = mask | bit
            
            # Option 1: do not change this character
            if new_mask.bit_count() > k:
                # Starting a new partition
                best = dfs(i + 1, bit, can_change) + 1
            else:
                # Continue in same partition
                best = dfs(i + 1, new_mask, can_change)
            
            # Option 2: change this character (if allowed)
            if can_change:
                for c in range(26):
                    changed_bit = 1 << c
                    nm = mask | changed_bit
                    if nm.bit_count() > k:
                        # change causes overflow → forced partition
                        best = max(best, dfs(i + 1, changed_bit, 0) + 1)
                    else:
                        # change keeps within limit
                        best = max(best, dfs(i + 1, nm, 0))
            
            return best
        
        return dfs(0, 0, 1)
