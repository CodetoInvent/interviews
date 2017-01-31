from tree import *
import sys

def min_depth(root):
    if not root: return 0

    if not root.left and not root.right:
        return 1

    left = min_depth(root.left) if root.left else sys.maxint
    right = min_depth(root.right) if root.right else sys.maxint
    return min(left, right) + 1


# def min_depth(root, depth, minimum):
#     if not root: return minimum

#     if not root.left and not root.right:
#         return min(minimum, depth)

#     minimum = min(minimum, min_depth(root.left, depth+1, minimum))
#     minimum = min(minimum, min_depth(root.right, depth+1, minimum))
#     return minimum



# print min_depth(root, 1, sys.maxint)

print min_depth(root)

def max_depth(root):
    if not root: return 0

    left = max_depth(root.left)
    right = max_depth(root.right)

    return max(left, right)+1

print max_depth(root)