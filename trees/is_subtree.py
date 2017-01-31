
class Node:
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None

def identical(root1, root2):
    if not root1 and not root2: return True

    if not root1 or not root2: return False

    return all([
        root1.data == root2.data, 
        identical(root1.left, root2.left),
        identical(root1.right, root2.right)
        ])

    
def is_subtree(tree, subtree):

    if not subtree: return True
    if not tree: return False

    if identical(tree, subtree): return True

    return is_subtree(tree.left, subtree) or subtree(tree.right, subtree)
    
 
""" TREE 1
     Construct the following tree
              26
            /   \
          10     3
        /    \     \
      4      6      3
       \
        30
    """
 
T = Node(26)
T.right = Node(3)
T.right.right  = Node(3)
T.left = Node(10)
T.left.left = Node(4)
T.left.left.right = Node(30)
T.left.right = Node(6)
 
""" TREE 2
     Construct the following tree
          10
        /    \
      4      6
       \
        30
    """
S = Node(10)
S.right = Node(6)
S.left = Node(4)
S.left.right = Node(30)
 
if is_subtree(T, S):
    print "Tree 2 is subtree of Tree 1"
else :
    print "Tree 2 is not a subtree of Tree 1"