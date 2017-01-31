
class Node(object):

    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return self.__str__()


class DoublyLinkedList(object):

    def __init__(self):
        self.head = None

    def check_head(self, data):
        if not self.head:
            self.head = Node(data)
            return True
        return False

    def addLast(self, data):
        if self.check_head(data): return 

        node = Node(data)
        tail = self.head

        while tail.next:
            tail = tail.next

        tail.next = node
        node.previous = tail


    def addFirst(self, data):
        if self.check_head(data): return 

        node = Node(data)
        head = self.head

        head.previous = node
        node.next = head
        self.head = node

    def search(self, data):
        node = self.head
        result = None

        while node:
            if node.data == data: 
                result = node
                break
            node = node.next
        
        return result

    def delete(self, data):
        node = self.search(data)
        if not node: return False

        next_node = node.next
        previous_node = node.previous

        if next_node:
            next_node.previous = previous_node

        if previous_node:
            previous_node.next = next_node

        if node == self.head:
            self.head = next_node
            

if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.addFirst(1)
    dll.addFirst(3)
    dll.addFirst(5)
    dll.addFirst(2)
    dll.addFirst(5)

    print dll.search(2)
    dll.delete(2)
    print dll.search(2)
    dll.addLast(2)
    print dll.search(2)





    
