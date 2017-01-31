from linkedlist import *


l1 = LinkedList()
l1.insert(1)
l1.insert(2)
l1.insert(3)
l1.insert(4)
l1.insert(5)

l2 = LinkedList()
l2.insert(2)
l2.insert(3)
l2.insert(4)
l2.insert(5)
l2.insert(6)
l2.insert(7)

l2.remove(7)
print l2


def merge(l1, l2):
    p1 = l1.head
    p2 = l2.head
    head = Node(0)
    p = head

    while p1 or p2:
        if p1 and p2:
            if p1.data < p2.data:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next
            p = p.next
        else:
            if p1:
                p.next = p1
            elif p2:
                p.next = p2
            break
    return head.next


node = merge(l1, l2)

while node:
    print node
    node = node.next

