
class Node():

    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return '({})'.format(self.data)


def add(a, b, carry):
    add = a + b + carry
    carry = add / 10
    add = add % 10
    return add, carry


def sum_lists(a, b):

    carry = 0
    root = None
    current = root

    while a or b:
        i = a.data if a else 0
        j = b.data if b else 0
        digit, carry = add(i, j, carry)

        if not root:
            root = Node(digit)
            current = root
        else:
            node = Node(digit)
            current.next = node
            current = current.next

        a = a.next if a else None
        b = b.next if b else None

    if carry: current.next = Node(carry)

    return root


if __name__ == '__main__':
    root1 = Node(7)
    second = Node(1)
    third = Node(9)
    root1.next = second
    second.next = third

    root2 = Node(5)
    second = Node(9)
    third = Node(2)
    fourth = Node(9)
    root2.next = second
    second.next = third
    third.next = fourth

    result = sum_lists(root1, root2)
    while result:
        print result
        result = result.next
