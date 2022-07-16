from dataclasses import dataclass
from hashlib import new


class Node:
    def __init__(self, data: str) -> None:
        self.data = data
        self.nextNode = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.numOfNodes = 0
    
    def insert_start(self, data):
        self.numOfNodes += 1
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.nextNode = self.head
            self.head = new_node
    
    
    def insert_end(self, data):
        self.numOfNodes += 1
        new_node = Node(data)
        current_node = self.head
        while current_node.nextNode is not None:
            current_node = current_node.nextNode
        
        current_node.nextNode = new_node
        
    def remove_node(self, data):
        if self.head is None:
            return
        
        current_node = self.head
        previous_node = None
        
        while current_node is not None and current_node.data != data  :
            previous_node = current_node
            current_node = current_node.nextNode
            
        if(current_node is None):
            return False
            
        if previous_node is None and current_node.nextNode is None:
            found_node = self.head
            self.head = None
            self.numOfNodes -= 1
            return found_node.data
            
        elif previous_node is None and current_node.nextNode is not None:
            self.head = current_node.nextNode
            self.numOfNodes -= 1
            return current_node.data
        else:
            previous_node.nextNode = current_node.nextNode
            self.numOfNodes -= 1
            return current_node.data
            
        
            
    
    def traverse(self):
        current_node = self.head
        while(current_node):
            print(current_node.data)
            current_node = current_node.nextNode
    
    def size_of_list(self):
        return self.numOfNodes
        


if __name__ == "__main__":
    
    linked_list = LinkedList()
    linked_list.insert_start(5)
    linked_list.insert_start(4)
    linked_list.insert_start(2)
    linked_list.insert_end(6)
    linked_list.insert_end(7)
    linked_list.traverse()
    size = linked_list.size_of_list()
    print('size of list is: ' + str(size))
    linked_list.remove_node(6)
    print('after removing 6')
    size = linked_list.size_of_list()
    print('size of list is: ' + str(size))
    linked_list.traverse()
    linked_list.remove_node(2)
    print('after removing 2')
    linked_list.traverse()
    linked_list.remove_node(7)
    print('after removing 7')
    linked_list.traverse()
    size = linked_list.size_of_list()
    print('size of list is: ' + str(size))
    data = linked_list.remove_node(8)
    if(not data):
        print('data not found')
        linked_list.traverse()
    else:
        print('data found')
        print('after removing 8')
        linked_list.traverse()
    size = linked_list.size_of_list()
    print('size of list is: ' + str(size))
    


    