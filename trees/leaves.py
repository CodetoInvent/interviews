from tree import *


def traverse(root, result):
    if not root: return
    if not root.left and not root.right:
        result.append(root)

    traverse(root.left, result)
    traverse(root.right, result)

    return result

print traverse(root, [])

