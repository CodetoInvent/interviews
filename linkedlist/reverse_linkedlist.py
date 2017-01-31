from linkedlist import *

def reverse_linked_list(ll):
    previous = next = None
    node = ll.head

    if not node: return None

    while node:
        next, node.next = node.next, previous
        previous, node = node, next

    ll.head = previous

    return ll

l = LinkedList()

l.insert('a')
l.insert('b')
l.insert('c')
l.insert('d')
print l

print reverse_linked_list(l)