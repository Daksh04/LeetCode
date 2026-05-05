# 61. Rotate List

# [Medium]

# Given the head of a linked list, rotate the list to the right by k places.

# Example 1:

# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]
# Example 2:

# Input: head = [0,1,2], k = 4
# Output: [2,0,1]
 
# Constraints:

# The number of nodes in the list is in the range [0, 500].
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 109

# Code: Python3

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        # Step 1: Find length and last node
        length = 1
        last = head
        
        while last.next:
            last = last.next
            length += 1
        
        # Step 2: Optimize k
        k = k % length
        if k == 0:
            return head
        
        # Step 3: Make it circular
        last.next = head
        
        # Step 4: Find new tail
        steps_to_new_tail = length - k
        new_tail = head
        
        for _ in range(steps_to_new_tail - 1):
            new_tail = new_tail.next
        
        # Step 5: Break the circle
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head

# Time Complexity: O(n)
# Space Complexity: O(1)
