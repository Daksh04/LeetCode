# 1382. Balance a Binary Search Tree

# [Medium]

# Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

# A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.

 

# Example 1:


# Input: root = [1,null,2,null,3,null,4,null,null]
# Output: [2,1,3,null,null,null,4]
# Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.
# Example 2:


# Input: root = [2,1,3]
# Output: [2,1,3]
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# 1 <= Node.val <= 105

# Code: Python 3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr=[]
        def inOrder( root):
            if not root: return
            inOrder(root.left)
            arr.append(root)
            inOrder(root.right)

        def balanceBST(l, r):
            if l>r: return None
            m=(l+r)>>1
            L=balanceBST(l, m-1)
            R=balanceBST(m+1, r)
            arr[m].left=L
            arr[m].right=R
            return arr[m]

        inOrder(root)
        return balanceBST(0, len(arr)-1)