from tree import *


def same(p, q):
    if not p and not q: return True
    if not p or not q: return False

    if p.data == q.data:
        return same(p.left, q.left) and same(p.right, q.right)
    else: return False

print same(root, root)