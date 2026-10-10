#insert a code at specific position in the linked list
def insert_at_position(head, new_node, position):
    if position == 0:
        new_node.next = head
        head = new_node
        return head

    current = head
    count = 0

    while current and count < position - 1:
        current = current.next
        count += 1

    if current is None:
        print("Position is out of bounds.")
        return head

    new_node.next = current.next
    current.next = new_node
    return head