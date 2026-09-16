# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow=head
        fast=head.next

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        right=slow.next
        slow.next=None

        prev=None

        while right:
            nxt=right.next
            right.next=prev
            prev=right
            right=nxt
        head1=head            
        head2=prev

        newhead=ListNode()
        curr=newhead
        flip=1

        while head2:
            if flip==1:
                curr.next=head1
                curr=curr.next
                head1=head1.next
                flip*=-1
            else:
                curr.next=head2
                curr=curr.next
                head2=head2.next
                flip*=-1
        if head1:
            curr.next=head1
                
            



        