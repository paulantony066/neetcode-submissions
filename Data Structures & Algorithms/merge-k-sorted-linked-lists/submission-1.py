# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def mergelist(h1,h2):
            d=ListNode()
            curr=d
            

            while h1 and h2:
                if h1.val<h2.val:
                    curr.next=h1
                    h1=h1.next
                else:
                    curr.next=h2
                    h2=h2.next
                curr=curr.next
            if h1:
                curr.next=h1
            elif h2:
                curr.next=h2
            return d.next
        if len(lists)==0:
            return None


                    
        while len(lists)>1:
            merged=[]
            for i in range(0,len(lists),2):
                if i+1>len(lists)-1:
                    l1=lists[i]
                    l2=None
                else:
                    l1=lists[i]
                    l2=lists[i+1]

                merged.append(mergelist(l1,l2))
            lists=merged

            
        return lists[0]
        
    
                    




        