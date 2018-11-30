from collections import deque
import drawtree

class Node():

    def __init__(self, data, right=None, left=None, parent=None):
        self.data = data
        self.right = right
        self.left = left
        self.parent = parent

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return '({})'.format(self.data)
    
    def draw(self):
        queue = deque()
        queue.append(self)
        result = []

        while queue:
            node = queue.popleft()
            string = str(node.data) if node else '#'
            result.append(string)
            
            if node: queue.append(node.left)
            if node: queue.append(node.right)

        serialized = ','.join(result)
        drawtree.draw_level_order(serialized)
        print

root = Node(6)
root.right = Node(7, parent=root)
root.right.right = Node(9, parent=root.right)
root.right.right.left = Node(8, parent=root.right.right)
root.left = Node(3, parent=root)
root.left.right = Node(4, parent=root.left)
root.left.right.right = Node(5, parent=root.left.right)
root.left.left = Node(1, parent=root.left)
root.left.left.left = Node(0, parent=root.left.left)
root.left.left.right = Node(10, parent=root.left.left)
