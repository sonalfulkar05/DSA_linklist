#find nth node from the end of a list
def find_nth_from_end(head, n):
    first = head
    second = head

    for _ in range(n):
        if not first:
            return None  
        first = first.next

    while first:
        first = first.next
        second = second.next

    return second.data