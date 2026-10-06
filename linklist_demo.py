#Singly linear linked list implementation in python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:
    def __init__(self):
        self.head = None
    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node #append new node at the end of the list            
    def print(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp=temp.next    
            

list = LinkList()
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
list.append(n1)
list.append(n2)
list.append(n3)
list.print()