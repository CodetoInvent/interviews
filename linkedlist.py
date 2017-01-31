class Node():

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():

    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            return

        tail = self.head
        while tail.next:
            tail = tail.next

        tail.next = node

    def search(self, k):
        p = self.head
        if not p:
            return None
        while p.next:
            if p.data == k:
                return p
            p = p.next
        return None

    def remove(self, k):
        if self.head.data == k:
            self.head = self.head.next
            return

        node = self.head
        while node.next:
            if node.next.data == k:
                node.next = node.next.next
                return
            node = node.next

    def __str__(self):
        p = self.head
        if not p: return '<empty>'
        
        s = self.head.data
        while p.next:
            p = p.next
            s += '-->' + p.data
        return s


l = LinkedList()

l.insert('a')
l.insert('b')
l.insert('c')
l.insert('d')
print l


def reverse_linked_list(ll):
    previous = next = None
    current = ll.head

    if not current: return None

    while current:
        next = current.next
        current.next = previous
        previous, current = current, next

    ll.head = previous

    print ll

reverse_linked_list(l)


# head = l.head
# def reverse_linked_list_recursive(node):

#     if not node.next: return node

#     head = reverse_linked_list_recursive(node.next)

#     node.next.next = node
#     node.next = None

# reverse_linked_list_recursive(l.head)
# print l


# detect if it has loop

# boolean hasLoop(Node first) {
#     Node slow = first;
#     Node fast = first;

#     while(fast != null && fast.next != null) {
#         slow = slow.next;          // 1 hop
#         fast = fast.next.next;     // 2 hops 

#         if(slow == fast)  // fast caught up to slow, so there is a loop
#             return true;
#     }
#     return false;  // fast reached null, so the list terminates
# }
