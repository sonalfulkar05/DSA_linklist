#delete node from the linked list
def delete_node(head, target):
    if head is None:
        return head
    if head.data == target:
        return head.next