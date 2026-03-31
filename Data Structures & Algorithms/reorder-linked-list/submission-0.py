# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head 
        fast = head.next  
        while fast and fast.next :
            slow = slow.next 
            fast = fast.next.next

        second = slow.next 
        slow.next = None   #split into 2 ll    need to reverse this second half 
        prev = None
        while second :
            nxt = second.next 
            second.next = prev 
            prev = second 
            second = nxt 


        first , second = head , prev  

        while second :
            temp1,temp2 = first.next , second.next 
            first.next = second 
            second.next = temp1
            first = temp1 
            second = temp2 





        
        