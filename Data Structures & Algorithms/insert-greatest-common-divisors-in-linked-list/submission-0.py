# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def insert(prev,nxt,node):
            temp=prev.next
            prev.next=node
            node.next=temp
            

        def gcd(a,b):
            while b:
                a,b=b,a%b
            return abs(a)

        if not head:
            return None

        curr=head

        while curr and curr.next:
            a=curr.val
            b=curr.next.val
            g=gcd(a,b)
            node=ListNode()
            node.val=g
            insert(curr,curr.next,node)
            curr=curr.next.next

        return head

        