# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr1=l1
        curr2=l2

        carry=0

        head=ListNode()
        curr3=head

        while curr1 or curr2 or carry:
            if curr1:
                num1=curr1.val
            else:
                num1=0
            if curr2:
                num2=curr2.val
            else:
                num2=0
            dig=num1+num2+carry
            carry=dig//10
            dig=dig%10
                

            curr3.next=ListNode(dig)

            curr3=curr3.next
            if curr1:
                curr1=curr1.next
            
            if curr2:
                curr2=curr2.next
            
        return head.next
