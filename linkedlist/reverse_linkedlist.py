from linkedlist import *

def reverse_linked_list(ll):
    previous = next = None
    current = ll.head

    if not current: return None

    while current:
        next = current.next,
        current.next = previous

        previous = current
        current = next

    ll.head = previous

    return ll

l = LinkedList()

l.insert('a')
l.insert('b')
l.insert('c')
l.insert('d')
print l

print reverse_linked_list(l)