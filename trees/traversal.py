from collections import deque
from tree import *


def preorder(node):
    if not node: return
    print node
    preorder(node.left)
    preorder(node.right)

# preorder(root)

def iterative_preorder(root):
    stack = []
    stack.append(root)

    while stack:
        node = stack.pop()
        print node
        if node.right: stack.append(node.right)
        if node.left: stack.append(node.left)

# iterative_preorder(root)

def inorder(node):
    if not node: return
    inorder(node.left)
    print node.data
    inorder(node.right)

# inorder(root)

def iterative_inorder(node):
    stack = []

    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            print node
            node = node.right

# iterative_inorder(root)

def postorder(node):
    if not node: return
    postorder(node.left)
    postorder(node.right)
    print node

# postorder(root)


def bfs(root):
    queue = deque()
    queue.append(root)

    while queue:
        node = queue.popleft()
        print node

        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)

# bfs(root)
