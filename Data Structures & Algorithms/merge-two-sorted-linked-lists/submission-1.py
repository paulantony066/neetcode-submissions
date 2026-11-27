# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        new=ListNode()
        ptr=new

        curr1=list1
        curr2=list2

        while curr1 and curr2:
            if curr1.val<curr2.val:
                ptr.next=curr1
                curr1=curr1.next
            else:
                ptr.next=curr2
                curr2=curr2.next
            ptr=ptr.next

        if curr1:
            while curr1:
                ptr.next=curr1
                curr1=curr1.next
                ptr=ptr.next
        if curr2:
            while curr2:
                ptr.next=curr2
                curr2=curr2.next
                ptr=ptr.next
        return new.next
                