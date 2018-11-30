from tree import *


# def invert(root):
# 	if not root: return
# 	root.left, root.right = root.right, root.left
# 	invert(root.left)
# 	invert(root.right)


# def invert_iterative(node):

# 	stack = [node]

# 	while stack:
# 		n = stack.pop(0)
# 		if not n: continue

# 		n.left, n.right = n.right, n.left
# 		stack.append(n.left)
# 		stack.append(n.right)



# root.draw()
# invert(root)
# root.draw()
# invert_iterative(root)
# root.draw()


def is_bst(node, minimum, maximum):
	if not node: return True

	if not node.data >= minimum and not node.data <= maximum: return False
	left = is_bst(node.left, minimum, node.data)
	right = is_bst(node.right, node.data, maximum)

	return left and right

print is_bst(root, -1000, 1000)
