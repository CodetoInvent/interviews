class Node():

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return '[{}]'.format(self.data)


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
            s += ' -> ' + str(p.data)
        return s



# class Node():

#     def __init__(self, value):
#         self.value = value
#         self.next = None

#     def __repr__(self):
#         return self.__str__()

#     def __str__(self):
#         return "[{value}]".format(value=self.value)


# class LinkedList():

#     def __init__(self):
#         self.head = None

#     def insert(self, new_node):
#         if self.head:
#             node = self.head
#             while node.next: 
#                 node = node.next
#             node.next = new_node
#         else:
#             self.head = new_node

#     def remove(self, value):
#         node = self.head
#         if node.value == value:
#             self.head = node.next
#             return
        
#         while node.next:
#             if node.next.value == value:
#                 node.next = node.next.next
#                 return
#             node = node.next

#     def __repr__(self):
#         return self.__str()

#     def __str__(self):
#         if not self.head: return "[empty]"
#         node = self.head
#         ll = str(node)

#         while node.next:
#             node = node.next
#             print node
#             ll += " -> " + str(node)

#         return ll


# if __name__ == '__main__':

#     node1 = Node(5)
#     node2 = Node(6)
#     node1.next = node2
#     assert str(node1) == "[5]"
#     assert str(node1.next) == "[6]"
#     assert node2.next == None


#     ll = LinkedList()
#     node1 = Node(5)
#     node2 = Node(6)

#     ll.insert(node1)
#     assert str(ll) == "[5]"
#     ll.insert(node2)
#     assert str(ll) == "[5] -> [6]"

#     # ll.remove(5)
#     # assert str(ll) == "[6]"
#     # node1 = Node(5)
#     # ll.add(node1)
#     print str(ll)