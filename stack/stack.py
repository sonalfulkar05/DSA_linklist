class Node:
    def __init__(self, value):
        self.data= value
        self.next = None

class stack:
    def __init__(self):
        self.top = None
    def isempty(self):
        if self.top is None:
            return True
        return False
    def push(self,new_node):
        new_node.next = self.top
        self.top = new_node
    def print(self):
        print("Stack elements are:")
        if self.isempty():
            print("Stack is empty")
            return    
        temp self.top
        while temp:
            print(temp.data)
            temp=temp.next
            
        