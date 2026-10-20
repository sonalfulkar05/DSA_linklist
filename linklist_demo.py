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
    def delete_node(self, target):
        if self.head is None:
            return
        if self.head.data == target:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == target:
                current.next = current.next.next
                return
            current = current.next
    def insert_at_position(self, new_node, prev_data):
        temp = self.head
        while temp:
            if temp.data == prev_data:
                break
            temp = temp.next
        if temp is None:
            print(f"Node with data {prev_data} not found.")        
            return
        new_node = Node(new_data)
        new_node.next = temp.next
        temp.next = new_node
    def sort(self):
        if self.head is None:
            return
        current = self.head
        while current:
            index = current.next
            while index:
                if current.data > index.data:
                    current.data, index.data = index.data, current.data
                index = index.next
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
list.delete_node(-20)
list.print()