"""
Leet Code 24: Swap Nodes in Pairs
https://leetcode.com/problems/swap-nodes-in-pairs/


Given a linked list, swap every two adjacent nodes and return its head.

Input: head = [1,2,3,4]
Output: [2,1,4,3]

Input: head = []
Output: []

Input: head = [1]
Output: [1]


Constraints:
The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100


Follow up: Can you solve the problem without modifying the values in the list's nodes? (i.e., Only nodes themselves may be changed.)

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        head.next.next, head.next, head = head, self.swapPairs(head.next.next), head.next
        return head
