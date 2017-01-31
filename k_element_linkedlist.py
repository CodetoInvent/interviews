
# Write a fundtion which returns kth element from the tail in a linked list.


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


    def k_element(self, k):
        pointer1 = self.head
        pointer2 = self.head

        for i in range(k):
            if pointer1.next: pointer1 = pointer1.next

        while pointer1.next:
            pointer1 = pointer1.next
            pointer2 = pointer2.next

        return pointer2





l = LinkedList()

l.insert('a')
l.insert('b')
l.insert('c')
l.insert('d')


print l.k_element(3).data
