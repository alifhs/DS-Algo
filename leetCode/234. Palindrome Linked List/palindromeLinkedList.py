# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return True
        
        currentNode = head
      
        prevNode = None
        nextNode = None
        forwardSum = 0;
        placeValue = 1;
        
        kontstant = 2
        while currentNode is not None:
            if prevNode is None:
                
                if(currentNode.val != 0):
                    forwardSum += currentNode.val *  placeValue
                    placeValue += 1
                else:
                    forwardSum += kontstant * placeValue
                    placeValue += 1
                    
                prevNode = currentNode
                currentNode = currentNode.next
                prevNode.next = None
                
            else :
                 if(currentNode.val != 0):
                        forwardSum += currentNode.val *  placeValue
                        placeValue += 1
                 else:
                    forwardSum += kontstant * placeValue
                    placeValue += 1
            
                 nextNode = currentNode.next
                 currentNode.next = prevNode
                 prevNode = currentNode
                 if nextNode is None:
                    head = currentNode
                 currentNode = nextNode
        
        backWardSum = 0;
        placeValue = 1
        
        while head is not None:
            if head.val != 0:
                backWardSum += head.val * placeValue
                placeValue += 1
            else:
                backWardSum += kontstant * placeValue
                placeValue += 1
            head = head.next
        # print(forwardSum)
        # print(backWardSum)
            
        return forwardSum == backWardSum
            
# TestCase 
           
# solution  = Solution()

# list1 = ListNode(1,ListNode(2,(ListNode(3 ,ListNode(4)))))

# assert solution.isPalindrome(list1) == False
# list2 = ListNode(1,ListNode(2,(ListNode(2 ,ListNode(1)))))

# assert solution.isPalindrome(list2) == True
# list3 = ListNode(1,ListNode(0,(ListNode(0))))

# # 2 2 3
# # 1 2 4
# assert solution.isPalindrome(list3) == False

# list2 = ListNode(1,ListNode(3,(ListNode(0 ,ListNode(2)))))

# assert solution.isPalindrome(list2) == False
# list4 = ListNode(0,(ListNode(0)))

# assert solution.isPalindrome(list4) == True

  
# x = 10 ** (10 ** 6)
# print('s')