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
    def count(self):
        temp = self.head
        count = 0
        while temp:
            if temp.data > 0:
                count += 1
            temp = temp.next
        return count        
    def alternate_print(self):
        temp = self.head
        while temp:
            print(temp.data)
            if temp.next:
                temp = temp.next.next
            else:
                break        
    def delete_alternate(self):
        if self.head is None:
            return
        current = self.head
        while current and current.next:
            current.next = current.next.next
            current = current.next
list = LinkList()
n1 = Node(10)
n2 = Node(-20)
n3 = Node(30)
n4= Node(-40)
list.append(n1)
list.append(n2)
list.append(n3)
list.append(n4)
list.print()
print("Number of nodes in the list:", list.count())
list.alternate_print()
list.print()
list.delete_alternate()
list.print()
list.print()