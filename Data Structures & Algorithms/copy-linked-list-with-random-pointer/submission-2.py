"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dic={}

        curr = head
        while curr:
            node=Node(x=curr.val)
            dic[curr]=node
            curr=curr.next
        
        curr=head

        while curr:
            node=dic[curr]
            if curr.next!=None:
                node.next=dic[curr.next]
            else:
                node.next=None
            
            if curr.random!=None:
                node.random=dic[curr.random]
            else:
                node.random=None
            curr=curr.next
        if head==None:
            return None
        return dic[head]
        
            

        