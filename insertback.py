#insert at the end of the linked list
def insert_at_end(head, new_node):
    if head is None:
        head = new_node
        return head
    