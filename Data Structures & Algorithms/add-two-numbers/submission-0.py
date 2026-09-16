# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr=l1

        num1=""

        while curr:
            num1+=str(curr.val)
            curr=curr.next
        num1=num1[::-1]
        
        
        curr=l2
        num2=""
        while curr:
            num2+=str(curr.val)
            curr=curr.next
        num2=num2[::-1]
        

        s=int(num1)+int(num2)
        s=str(s)
        s=s[::-1]

        head=None
        curr=None
        
        for i in range(len(s)):
            node=ListNode(s[i])
            if head==None:
                head=node
                curr=node
            else:
                curr.next=node
                curr=node
        return head

            

        
            
        