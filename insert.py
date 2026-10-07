#insert at the beginning of the linked list
def insert_at_beginning(head, new_node):
    new_node.next = head
    head = new_node
    return head
