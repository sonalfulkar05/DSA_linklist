# Create a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create linked list
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)

# Link the nodes
n1.next = n2
n2.next = n3

# Traverse and print node values
temp = n1

while temp is not None:
    print(temp.data)
    temp = temp.next