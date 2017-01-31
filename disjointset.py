
class Node():

    def __init__(self, data, parent = None, rank = 0):
        self.data = data 
        self.parent = parent 
        self.rank = rank

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return self.__str__()

class DisjointSet():

    def __init__(self):
        self.nodes = {}

    def make_set(self, data):
        node = Node(data)
        node.parent = node
        self.nodes[data] = node

    def find(self, node):
        parent = node.parent

        if node == parent:
            return node

        node.parent = self.find(parent)
        return node.parent


    def find_set(self, data):
        if data not in self.nodes: return None
        node = self.nodes[data]
        return self.find(node)

    def union(self, data1, data2):
        
        parent1 = self.find_set(data1)
        parent2 = self.find_set(data2)

        if parent1 == None or parent2 == None: return

        if parent1 == parent2: return

        if parent1.rank >= parent2.rank:
            if parent1.rank == parent2.rank:
                parent1.rank += 1
            parent2.parent = parent1
        else:
            parent1.parent = parent2


ds = DisjointSet()
ds.make_set(1)
ds.make_set(2)
ds.make_set(3)
ds.make_set(4)
ds.make_set(5)
ds.make_set(6)
ds.make_set(7)

ds.union(1,2)
ds.union(2,3)
ds.union(4,5)
ds.union(6,7)
ds.union(5,6)
ds.union(3,7)

for i in range(1,8):
    print(ds.find_set(i))

