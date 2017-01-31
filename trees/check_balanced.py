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

def height(root):
    if not root: return 0
    return 1 + max(height(root.left), height(root.right))


def balanced(root):
    if not root: return True

    left_height = height(root.left)
    right_height = height(root.right)

    return abs(left_height - right_height) <= 1 and \
        balanced(root.left) and \
        balanced(root.right)


print balanced(root)