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
        self.numOfNodes = self.numOfNodes + 1
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.nextNode = self.head
            self.head = new_node
    
    def print_elements(self):
        current_node = self.head
        while(current_node):
            print(current_node.data)
            current_node = current_node.nextNode
        


# if __name__ == "main":
    
linked_list = LinkedList()
linked_list.insert_start(5)
linked_list.insert_start(4)
linked_list.insert_start(2)
linked_list.print_elements()

    