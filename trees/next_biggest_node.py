from tree import *


def next_biggest_node(node):
    if node.right:
        node = node.right
        while node.left:
            node = node.left
        return node
    if not node.parent:
        return None
    while node.parent:
        if node.parent.left == node:
            return node.parent
        node = node.parent
    return None

print next_biggest_node(root.right.right) # biggest node -> None
print next_biggest_node(root.right) # has right child -> 8
print next_biggest_node(root.left.right.right) # has no right child -> 6
