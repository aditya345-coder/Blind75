# Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

"""Problem Description:
Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""


## Solution 1: Time Complexity: O(n); Space Complexity: O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head; length=0

        while(curr is not None):
            length+=1
            curr=curr.next
        
        curr2=head
        if (length==n):
            return head.next

        for i in range(length-1-n):
            curr2=curr2.next
        
        curr2.next=curr2.next.next

        return head


# Solution 2:  Time Complexity: O(n); Space Complexity: O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow=head; fast=head
        for _ in range(n):
            fast=fast.next
        if not fast:
            return head.next

        while fast.next:
            fast=fast.next
            slow=slow.next
        
        slow.next=slow.next.next

        return head
