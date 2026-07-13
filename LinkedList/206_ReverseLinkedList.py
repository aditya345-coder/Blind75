# Link: https://leetcode.com/problems/reverse-linked-list/description/

"""Problem Description:
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""

# Solution: Time Complexity: O(n); Space Complexity: O(n)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head==None or head.next==None):
            return head
        curr=head
        prev=None

        while(curr is not None):
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        
        return prev
