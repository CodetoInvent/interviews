from tree import *

# private int checkHeight(Node root) throws IllegalArgumentException {
#     if (root == null) return -1;
#     int leftHeight = checkHeight(node.left);
#     int rightHeight = checkHeight(node.right);

#     if (Math.abs(leftHeight - rightHeight) > 1){
#         throw new IllegalArgumentException();
#     }

#     return Math.max(leftHeight, rightHeight);
# }

def height(node):
  if not node: return 0
  return 1 + max(
    height(node.left),
    height(node.right)
  )

def check_balanced(tree):
  if not tree: return True

  left = height(tree.left)
  right = height(tree.right)
  height_diff = abs(left - right)
  return all([
    height_diff < 2,
    check_balanced(tree.left),
    check_balanced(tree.right)
  ])

print check_balanced(root)