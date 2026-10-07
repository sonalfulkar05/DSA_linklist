#search an element in the linked list
def search_element(head, target):
    current = head
    while current:
        if current.data == target:
            return True
        current = current.next
    return False