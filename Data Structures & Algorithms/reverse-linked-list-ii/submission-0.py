# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummy=ListNode(val=None,next=head)
        curr=head
        prev=dummy

        for i in range(left-1):
            prev=curr
            curr=curr.next

        #leftsave
        prev.next=None

        leftptr=curr

        

        for i in range(right-left):
            curr=curr.next

        rightptr=curr
        rightsave=rightptr.next
        rightptr.next=None


        hed=leftptr
        pre=None
        curr=hed

        while curr:
            nxt=curr.next
            curr.next=pre
            pre=curr
            curr=nxt
        prev.next=pre
        hed.next=rightsave

        return dummy.next

        
        

        
        
        

        





        