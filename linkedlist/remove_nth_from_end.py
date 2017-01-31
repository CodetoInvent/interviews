from linkedlist import *

l1 = LinkedList()
l1.insert(1)
l1.insert(2)
l1.insert(3)
l1.insert(4)
l1.insert(5)

print l1

# fix this
def remove_nth(ll, n):
  p1 = ll.head
  p2 = ll.head
  head = ll.head

  for i in range(n):
    if not p1: return None
    p1 = p1.next

  # remove head
  if not p1: return head.next

  while p1:
    p1, p2 = p1.next, p2.next

  p2.next = p2.next.next

  return head

print remove_nth(l1, 1)
