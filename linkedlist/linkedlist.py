class Node():

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return '({})'.format(self.data)


class LinkedList():

    def __init__(self):
        self.head = None

    def insert(self, data, is_node=False):
        if is_node: node = data
        else: node = Node(data)
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
        while p:
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

        s = str(self.head.data)
        while p.next:
            p = p.next
            s += '-->' + str(p.data)
        return s