from tree import *


def create(arr, start, end):
    if start > end: return None
    middle = (start + end) // 2
    root = Node(arr[middle])
    root.left = create(arr, start, middle-1)
    root.right = create(arr, middle+1, end)

    return root
    

def bst(arr):
    if not arr: return []
    return create(arr, 0, len(arr)-1)


bst([1,2,3,4,5,6,7]).draw()

