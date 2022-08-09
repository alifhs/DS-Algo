# Definition for singly-linked list.


from typing import List


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def findNode(self, list ,nodeToBeFound):
        for node in list:
            if node is nodeToBeFound:
                return node
        return None
            
    
    def detectCycle(self, head):
        
        currentNode = head
        
        found = None
        nodeList = []
        while(currentNode != None):
            
            if(self.findNode(nodeList, currentNode) != None):
                found = currentNode
                return found
            nodeList.append(currentNode)
            currentNode = currentNode.next
        
        return found
    
    # def createLinkedList(self, list : List[int]) -> ListNode:
    #     head = ListNode(list[0])
    #     currentNode = head
    #     for i in range(1, len(list)):
    #         currentNode.next = ListNode(list[i])
    #         currentNode = currentNode.next
    #     currentNode.next = head.next
    #     return head
    
    # def printLinkedList(self, list: ListNode):
        
        
    #     current = list;
    #     i = 0
    #     while(current != None) :
    #         print(current.val)
    #         current = current.next
    #         i += 1
    #         if(i > 7 ):
    #             break
            
            
# solution = Solution()
# # list = solution.createLinkedList([1,2,3,4,5])
# list = solution.createLinkedList([3,2,0,-4])
# # solution.printLinkedList(list)
# assert solution.detectCycle(list) is list.next
# x = solution.detectCycle(list)
# print(x.val)

# assert solution.detectCycle(list).val == 2

        
        
        
        