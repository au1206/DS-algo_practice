"""
Leet Code 530: Minimum Absolute Difference in BST
https://leetcode.com/problems/minimum-absolute-difference-in-bst/

Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

Example 1:
Input: root = [4,2,6,1,3]
Output: 1

Example 2:
Input: root = [1,0,48,null,null,12,49]
Output: 1


Constraints:
The number of nodes in the tree is in the range [2, 104].
0 <= Node.val <= 105
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # get in order, then take the min of pairwise differences
    def getMinimumDifference(self, root: TreeNode) -> int:
        visited = []
        res = 1000000000000

        def traverse(node):
            if node:
                traverse(node.left)
                visited.append(node.val)
                traverse(node.right)

        traverse(root)
        for i in range(1, len(visited)):
            res = min(res, abs(visited[i] - visited[i - 1]))

        return res

# Time is O(n) and Space is O(n)

# ALTERNATE: source LC discussions
# Keep track of the lo and hi bounds of each node, when you've passed the leaf nodes, compute hi - lo to get the lowest difference along that path


class Solution(object):
    def getMinimumDifference(self, root):
        def fn(node, lo, hi):
            if not node:
                return hi - lo

            left = fn(node.left, lo, node.val)
            right = fn(node.right, node.val, hi)

            return min(left, right)

        return fn(root, float('-inf'), float('inf'))

