# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        currentNode = head
      
        prevNode = None
        nextNode = None
        while currentNode is not None:
            if prevNode is None:
                prevNode = currentNode
                currentNode = currentNode.next
                prevNode.next = None
                
            else :
                nextNode = currentNode.next
                currentNode.next = prevNode
                prevNode = currentNode
                if nextNode is None:
                    head = currentNode
                currentNode = nextNode
        return head
            
            
           
            
            