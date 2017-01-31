from tree import *

def next_smallest_node(node):
  if not node: return None

  if node.left:
    node = node.left
    while node.right:
      node = node.right
    return node
  if not node.parent:
    return None
  while node.parent:
    if node.parent.right == node:
      return node
    node = node.parent
  return None

print next_smallest_node(root.right)