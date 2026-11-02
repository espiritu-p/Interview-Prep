# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        cur = head
        prev = None
        while cur is not None:
            n = cur.next    # save the remaining list
            cur.next = prev # reverse one link
            prev = cur      # move prev
            cur = n         # move cur

        return prev
