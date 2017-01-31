from tree import *
import sys

def is_bst(node, maximum, minimum):
  if not node: return True

  if node.data >= maximum or node.data <= minimum:
    return False

  left = is_bst(node.left, node.data, minimum)
  right = is_bst(node.right, maximum, node.data)

  return left and right

print is_bst(root, sys.maxint, -sys.maxint-1)
