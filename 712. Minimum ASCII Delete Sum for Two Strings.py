# 712. Minimum ASCII Delete Sum for Two Strings

# [Medium]

# Given two strings s1 and s2, return the lowest ASCII sum of deleted characters to make two strings equal.

 

# Example 1:

# Input: s1 = "sea", s2 = "eat"
# Output: 231
# Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
# Deleting "t" from "eat" adds 116 to the sum.
# At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.
# Example 2:

# Input: s1 = "delete", s2 = "leet"
# Output: 403
# Explanation: Deleting "dee" from "delete" to turn the string into "let",
# adds 100[d] + 101[e] + 101[e] to the sum.
# Deleting "e" from "leet" adds 101[e] to the sum.
# At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
# If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.
 

# Constraints:

# 1 <= s1.length, s2.length <= 1000
# s1 and s2 consist of lowercase English letters.

# Code: Python 3

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n1, n2=len(s1), len(s2)
        if n1<n2:
            return self.minimumDeleteSum(s2, s1)
        dp = [[0]*(n2+1) for _ in range(2)]
        for x in range(n1-1, -1, -1):
            par=x&1
            prev=1-par
            for y in range(n2-1, -1, -1):
                if s1[x]==s2[y]:
                    dp[par][y]=ord(s1[x]) + dp[prev][y+1]
                else:
                    dp[par][y]=max(dp[prev][y], dp[par][y+1])
        AsciiSum = 0
        for c in s1: AsciiSum += ord(c)
        for c in s2: AsciiSum += ord(c)

        return AsciiSum - 2*dp[0][0]