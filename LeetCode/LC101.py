"""
Leet Code 101: Symmetric Tree
https://leetcode.com/problems/symmetric-tree/


Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Input: root = [1,2,2,3,4,4,3]
Output: true


Input: root = [1,2,2,null,3,null,3]
Output: false


Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # root1 == root2
        # root1.left == root2.right
        # root1.right == root2.left
        def isMirror(root1, root2):
            if root1 is None and root2 is None:
                return True
            if root1 is not None and root2 is not None:
                if root1.val == root2.val:
                    return (isMirror(root1.left, root2.right) and isMirror(root1.right, root2.left))

            return False

        return isMirror(root, root)
