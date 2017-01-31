 from tree import *

# public class LowestCommonAncestorInBinaryTree {

#     public Node lca(Node root, Node n1, Node n2){
#         if(root == null){
#             return null;
#         }
#         if(root == n1 || root == n2){
#             return root;
#         }

#         Node left = lca(root.left, n1, n2);
#         Node right = lca(root.right, n1, n2);

#         if(left != null && right != null){
#             return root;
#         }
#         return left != null ? left : right;
#     }
# }

def lca(root, p, q):
    if not root: return None

    if root.data == p or root.data == q:
        return root

    left = lca(root.left, p, q)
    right = lca(root.right, p, q)

    if left and right: return root

    return left if left else right


print lca(root, 5, 7) # -> 6
print lca(root, 5, 4) # -> 4
print lca(root, 1, 4) # -> 3
