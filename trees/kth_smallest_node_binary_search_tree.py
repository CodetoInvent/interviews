from tree import *


def inorder(root, k):
    stack = []
    counter = 0

    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            counter += 1
            if counter == k: return root
            root = root.right

print inorder(root, 2)