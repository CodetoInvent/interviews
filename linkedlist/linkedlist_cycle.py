from linkedlist import *

l = LinkedList()

cycle = Node('b')
l.insert('a')
l.insert(cycle, True)
l.insert('c')
l.insert('d')
l.insert('e')
l.insert('f')
l.insert(cycle, True)



def has_cycle(ll):
    slow = ll.head
    fast = ll.head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast: return True

    return False

print has_cycle(l)



def count_cycle_len(ll):
    slow = ll.head
    fast = ll.head
    is_counting = False
    count = 0

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            if is_counting: return count
            else: is_counting = True

        if is_counting: count += 1

    return 0

print count_cycle_len(l)



def find_cycle_start(ll):
    def find_meeting_point():
        slow = ll.head
        fast = ll.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast: return slow

        return None

    def find_intersection(node):
        if not node: return None
        start = ll.head

        while start and node:
            start = start.next
            node = node.next

            if start == node: return node

        return None

    node = find_meeting_point()
    node = find_intersection(node)
    return node


print find_cycle_start(l)
