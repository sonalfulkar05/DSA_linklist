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
        
        