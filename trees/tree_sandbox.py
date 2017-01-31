from tree import *


# def lca(node, p, q):
#   if node.data > max(p, q):
#     return lca(node.left, p, q)
#   elif node.data < min(p, q):
#     return lca(node.right, p, q)
#   else: return node

# print lca(root, 3, 7)

# def find(root, p):
#   if not root: return None

#   if root.data > p:
#     return find(root.left, p)
#   elif root.data < p:
#     return find(root.right, p)
#   else: return root

# print find(root, 11)


# def lca(root, p, q):

#   if not root: return None

#   if root.data == p or root.data == q:
#     return root

#   left = lca(root.left, p, q)
#   right = lca(root.right, p, q)

#   if left and right: return root

#   return left if left else right

# print lca(root, 3, 7)


def path(root, current, paths):
  if not root: return
  current.append(root)
  if not root.left and not root.right:
    paths.append(current)
  else:
    path(root.left, current[::], paths)
    path(root.right, current[::], paths)

  return paths

print [sum(map(lambda x: x.data, i)) for i in path(root, [], [])]
# print path(root, [], [])
