# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow , fast = head , head.next 
        while fast and fast.next :
            slow = slow.next 
            fast = fast.next.next 
        
        secondH = slow.next 
        slow.next = None   #remove this second half from the ll 
        # we need to rerverse this second half 
        prev = None 
        while secondH:
            nxt = secondH.next 
            secondH.next = prev 
            prev = secondH
            secondH = nxt    
            #prev will be the new head 


        first,second = head , prev  
        while second : #second could be equal or less than 
            temp1,temp2 = first.next , second.next 
            first.next = second 
            second.next = temp1 
            first = temp1
            second = temp2




