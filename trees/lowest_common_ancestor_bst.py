from tree import *

# lowest common ancestor bst
# public Node lowestCommonAncestor(Node root, int p, int q) {
#     if (root.data > Math.max(p, q)) {
#         return lowestCommonAncestor(root.left, p, q);
#     } else if (root.data < Math.min(p, q)) {
#         return lowestCommonAncestor(root.right, p, q);
#     } else {
#         return root;
#     }
# }

def lca(root, p, q):
    if root.data > max(p, q):
        return lca(root.left, p, q)
    elif root.data < min(p, q):
        return lca(root.right, p, q)
    else: return root

print lca(root, 5, 7) # -> 6
print lca(root, 5, 4) # -> 4
print lca(root, 1, 4) # -> 3