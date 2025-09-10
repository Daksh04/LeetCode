#Problem 1733: Minimum Number of People to Teach
# On a social network consisting of m users and some friendships between users, two users can communicate with each other if they know a common language.

# You are given an integer n, an array languages, and an array friendships where:

# There are n languages numbered 1 through n,
# languages[i] is the set of languages the i​​​​​​th​​​​ user knows, and
# friendships[i] = [u​​​​​​i​​​, v​​​​​​i] denotes a friendship between the users u​​​​​​​​​​​i​​​​​ and vi.
# You can choose one language and teach it to some users so that all friends can communicate with each other. Return the minimum number of users you need to teach.

# Note that friendships are not transitive, meaning if x is a friend of y and y is a friend of z, this doesn't guarantee that x is a friend of z.
 

# Example 1:

# Input: n = 2, languages = [[1],[2],[1,2]], friendships = [[1,2],[1,3],[2,3]]
# Output: 1
# Explanation: You can either teach user 1 the second language or user 2 the first language.
# Example 2:

# Input: n = 3, languages = [[2],[1,3],[1,2],[3]], friendships = [[1,4],[1,2],[3,4],[2,3]]
# Output: 2
# Explanation: Teach the third language to users 1 and 3, yielding two users to teach.

# Code: Python 3
from typing import List
from collections import defaultdict

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        # Step 1: Convert each person's known languages into sets for fast intersection
        lang_sets = [set(l) for l in languages]
        
        # Step 2: Find candidates (people who cannot communicate with their friend)
        candidates = set()
        for u, v in friendships:
            if not (lang_sets[u - 1] & lang_sets[v - 1]):  # no common language
                candidates.add(u - 1)
                candidates.add(v - 1)
        
        # If all friendships already work, no need to teach anyone
        if not candidates:
            return 0
        
        # Step 3: Count how many candidates already know each language
        lang_count = defaultdict(int)
        for person in candidates:
            for lang in lang_sets[person]:
                lang_count[lang] += 1
        
        # Step 4: Best language to teach = one that most candidates already know
        max_known = max(lang_count.values())
        
        # Step 5: Remaining need to be taught
        return len(candidates) - max_known
        
# Code: Python
class Solution(object):
    def minimumTeachings(self, n, languages, friendships):
        """
        :type n: int
        :type languages: List[List[int]]
        :type friendships: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        
        # Step 1: Convert each person's known languages into sets for fast intersection
        lang_sets = [set(l) for l in languages]
        
        # Step 2: Find candidates (people who cannot communicate with their friend)
        candidates = set()
        for u, v in friendships:
            if not (lang_sets[u - 1] & lang_sets[v - 1]):  # no common language
                candidates.add(u - 1)
                candidates.add(v - 1)
        
        # If all friendships already work, no need to teach anyone
        if not candidates:
            return 0
        
        # Step 3: Count how many candidates already know each language
        lang_count = defaultdict(int)
        for person in candidates:
            for lang in lang_sets[person]:
                lang_count[lang] += 1
        
        # Step 4: Best language to teach = one that most candidates already know
        max_known = max(lang_count.values())
        
        # Step 5: Remaining need to be taught
        return len(candidates) - max_known        
