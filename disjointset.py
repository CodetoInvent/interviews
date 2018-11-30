class Node():

    def __init__(self, value, rank = 0):
        self.value = value
        self.rank = rank

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "(%s)" % self.value



class DisjointSet():

    def __init__(self):
        self.nodes = {}

    def make_set(self, value):
        if value in self.nodes: return None

        node = Node(value)
        node.parent = node
        self.nodes[value] = node

    def find_set(self, value):
        if not value in self.nodes: return None

        node = self.nodes[value]

        while node.parent != node:
            node = node.parent

        return node

    def union(self, a, b):

        i = self.find_set(a)
        j = self.find_set(b)

        if not i or not j: return None

        if i.rank >= j.rank:
            j.parent = i
            i.rank += 1
        else:
            i.parent = j
            j.rank += 1


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
print vars(ds.nodes[1])


for i in range(1,8):
    print(i, ds.find_set(i))
