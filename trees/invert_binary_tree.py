from collections import deque
from tree import *


def invert_recursive(root):
    def invert(node):
        node.left, node.right = node.right, node.left

        if node.left: invert(node.left)
        if node.right: invert(node.right)

    if root: invert(root)
    return root

# invert_recursive(root).draw()


def invert_iterative(root):

    queue = deque()
    queue.append(root)

    while queue:
        node = queue.popleft()
        node.left, node.right = node.right, node.left

        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)

    return root

invert_iterative(root).draw()

