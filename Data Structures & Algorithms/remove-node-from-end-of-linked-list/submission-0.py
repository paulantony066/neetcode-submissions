# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        curr=head
        prev=None

        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        
        head2=prev

        curr2=head2
        count=1
        previous=None

        while curr2 and count!=n:
            previous=curr2
            curr2=curr2.next
            count+=1
        if count==n:
            if previous==None:
                head2=curr2.next
            else:
                previous.next=curr2.next

        
        curr=head2
        prev=None

        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        return prev
        

    

        