
from tree import *


root = Node(6)
root.right = Node(6, parent=root)
root.right.right = Node(9, parent=root.right)
root.right.right.left = Node(8, parent=root.right.right)
root.left = Node(3, parent=root)
root.left.right = Node(4, parent=root.left)
root.left.right.right = Node(5, parent=root.left.right)
root.left.left = Node(1, parent=root.left)
root.left.left.left = Node(0, parent=root.left.left)
root.left.left.right = Node(2, parent=root.left.left)
root.draw()

def traverse(node, paths, current, target):
    if not node: return
    current.append(node.data)
    new_target = target - node.data

    if new_target == 0: paths.append(current)

    traverse(node.left, paths, current[::], new_target)
    traverse(node.right, paths, current[::], new_target)

    return paths

print traverse(root, [], [], 12)



def all_leaf_paths(node, paths, current):
    if not node: return
    current.append(node.data)
    if not node.left and not node.right:
        paths.append(current)
    else:
        all_leaf_paths(node.left, paths, current[::])
        all_leaf_paths(node.right, paths, current[::])

    return paths

print all_leaf_paths(root, [], [])
