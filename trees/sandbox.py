from tree import *

def invert(root):

  if not root: root
  root.left, root.right = root.right, root.left
  if root.left: invert(root.left)
  if root.right: invert(root.right)
  return root

invert(root).draw()