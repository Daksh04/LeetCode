# 3714. Longest Balanced Substring II

# [Medium]

# You are given a string s consisting only of the characters 'a', 'b', and 'c'.

# A substring of s is called balanced if all distinct characters in the substring appear the same number of times.

# Return the length of the longest balanced substring of s.

 

# Example 1:

# Input: s = "abbac"

# Output: 4

# Explanation:

# The longest balanced substring is "abba" because both distinct characters 'a' and 'b' each appear exactly 2 times.

# Example 2:

# Input: s = "aabcc"

# Output: 3

# Explanation:

# The longest balanced substring is "abc" because all distinct characters 'a', 'b' and 'c' each appear exactly 1 time.

# Example 3:

# Input: s = "aba"

# Output: 2

# Explanation:

# One of the longest balanced substrings is "ab" because both distinct characters 'a' and 'b' each appear exactly 1 time. Another longest balanced substring is "ba".

 

# Constraints:

# 1 <= s.length <= 105
# s contains only the characters 'a', 'b', and 'c'.

# Code: Python 3

class Solution:
    def longestBalanced(self, s: str) -> int:
        n=len(s)
        # Deal with 1-letter balance
        ans, Len=1, 1
        for c0, c1 in pairwise(s):
            if c0==c1: Len+=1
            else:
                ans=max(ans, Len)
                Len=1
        ans=max(ans, Len)

        ab, bc, ca, abc={},{},{},{}
        abc[(0, 0)]=ab[(0, 0)]=bc[(0, 0)]=ca[(0, 0)]=-1

        cnt=[0, 0, 0]
        for i, c in enumerate(s):
            cnt[ord(c)-97]+=1
            A, B, C=cnt

            # 3-letter balance: A=B=C
            key=(B-A, C-A)
            if  key in abc: ans=max(ans, i-abc[key])
            else: abc[key]=i

            # 2-letter balance:
            key=(A-B, C)
            if  key in ab: ans=max(ans, i-ab[key])
            else: ab[key]=i

            key=(B-C, A)
            if  key in bc: ans=max(ans, i-bc[key])
            else: bc[key]=i

            key=(C-A, B)
            if  key in ca: ans=max(ans, i-ca[key])
            else: ca[key]=i
        return ans    