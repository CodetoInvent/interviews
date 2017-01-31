# Queue represented by two stacks

class MyQueue(object):

    def __init__(self):
        self.first = []
        self.second = []

    def put(self, data):
        self.first.append(data)

    def pop(self):
        self.shift()
        return self.second.pop()

    def shift(self):
        if not self.second:
            while self.first:
                data = self.first.pop()
                self.second.append(data)

    def peek(self):
        self.shift()
        return self.second[-1]


queue = MyQueue()
queue.put(2)
queue.put(3)
queue.put(4)
queue.put(5)
queue.put(6)
print queue.pop()
print queue.peek()
