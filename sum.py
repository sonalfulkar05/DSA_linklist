class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create linked list
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)

n1.next = n2
n2.next = n3
n3.next = n4

# Calculate consecutive sums
temp = n1

while temp is not None and temp.next is not None:
    total = temp.data + temp.next.data
    print(total)
    temp = temp.next