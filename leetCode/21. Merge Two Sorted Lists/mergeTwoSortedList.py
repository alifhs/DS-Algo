# Definition for singly-linked list.



# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        
        if list1.val <= list2.val:
             head1List1 = list1
             head2List2 = list2
        else:
            head1List1 = list2
            head2List2 = list1
        
       
        currentNodeList1 = head1List1
        currentNodeList2 = head2List2
        
        # print('list1', currentNodeList1.val)
        # print('list2', currentNodeList2.val)
        # i = 0
        while currentNodeList1 is not None:
            
            while currentNodeList2 and \
                (currentNodeList2.val >= currentNodeList1.val \
                    and(( currentNodeList1.next and \
                        ( currentNodeList2.val <= currentNodeList1.next.val))) or \
                            currentNodeList1.next is None):
                # print('list1', currentNodeList1.val)
                # print('list2', currentNodeList2.val)

                # if(i == 5):
                #     return
                # i += 1
                
                prevNextCurrentNodeList1 = currentNodeList1.next
                prevNextCurrentNodeList2 = currentNodeList2.next
                currentNodeList1.next = currentNodeList2
                currentNodeList1 = currentNodeList1.next
                currentNodeList1.next = prevNextCurrentNodeList1
                currentNodeList2 = prevNextCurrentNodeList2
                
                
                # print('after update---------')
                # print('list1', currentNodeList1.val)
                # print('list2', currentNodeList2.val)
                # currentNodeList1.next.next = current1Temp.next
                
            
            
            currentNodeList1 = currentNodeList1.next
        
        return head1List1
            
            
        
  
       
            

# def printNodes(list1: ListNode):
#     currentNode = list1
#     while(currentNode is not None):
#         print(currentNode.val)
#         currentNode = currentNode.next 
    

# solution = Solution()
# list1 = ListNode(1, ListNode(2, ListNode(4)))
# list2 = ListNode(0, ListNode(3, ListNode(4)))
# list3 = ListNode(1, ListNode(2, ListNode(4)))
# printNodes(list1)
# def mapNodeToList(list1: ListNode):
#     currentNode = list1
#     list = []
#     while(currentNode is not None):
#         # print(currentNode.val)
#         list.append(currentNode.val)
#         currentNode = currentNode.next
        
#     return list

# assert solution.mergeTwoLists(list1, list2) != None
# head, index = solution.getListLessThanCurrent(list3, 4) 
# printNodes(head)
# assert mapNodeToList(head) == [1, 2, 4]
# printNodes(list1)

# print('list2')

# printNodes(list4)

# assert solution.mergeTwoLists(None, None) == None
# assert mapNodeToList(list1) == [1, 2, 4]
# list4 =  solution.mergeTwoLists(list1, list2)
# assert mapNodeToList(list4) == [0, 1, 2, 3, 4, 4]

# list5 = ListNode(0)
# list6 = ListNode(1, ListNode(3, ListNode(4, ListNode(5))))

# list7 = solution.mergeTwoLists(list5, list6)
# # printNodes(list7)

# # print('-----------')
# assert mapNodeToList(list7) == [0, 1, 3, 4, 5]

# list8 = None
# list9 = ListNode(1, ListNode(2, ListNode(4)))
# list10 = solution.mergeTwoLists(list8, list9)

# assert mapNodeToList(list10) == [1, 2, 4]

# list11 = ListNode(1)
# list12 = ListNode(2, ListNode(6))

# list13 = solution.mergeTwoLists(list11, list12)
# # printNodes(list13)
# assert mapNodeToList(list13) == [1, 2,6]



            
                
            
        
        


#   def getListLessThanCurrent(self, head, current):
#         newList = None
#         newListCurrentNode = None
#         currentNode = head
#         while(currentNode is not None):
#             if(currentNode.val <= current):
#                 # print(currentNode.val)
#                 if(newList is None):
#                     # newList = ListNode(currentNode.val)
#                     newList = currentNode
#                     newListCurrentNode = newList
#                     currentNode = currentNode.next
#                 else:
#                     newListCurrentNode.next = currentNode
#                     newListCurrentNode = newListCurrentNode.next
#                     currentNode  = currentNode.next
#             else:
#                 break
#         newListCurrentNode.next = None
#         # print(newListCurrentNode.val)
#         return [newList , newListCurrentNode]
        
        