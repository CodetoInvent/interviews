from linkedlist import *

def reverse_linked_list(ll):
    previous = next_node = None
    current = ll.head

    if not current: return None

    while current:
        next_node, current.next = current.next, previous

        previous, current = current, next_node


    ll.head = previous

    return ll

l = LinkedList()

l.insert('a')
l.insert('b')
l.insert('c')
l.insert('d')
print l

print reverse_linked_list(l)