# https://www.pramp.com/question/jKoA5GAVy9Sr9jGBjz04
# Given an array of sorted distinct integers named arr, write a function that returns an index i in arr for which arr[i] = i or -1 if no such index exists.

def index_binary_search(arr):

    right = len(arr)-1
    left = 0

    while left <= right:
        mid = (right + left)//2
        value = arr[mid]
        if value > mid: right = mid-1
        elif value < mid: left = mid+1
        elif value == mid: return mid

    return -1



arr = [-8, 0, 1, 2, 4]
print index_binary_search(arr)


def binary_search(arr, num):
    right, left = len(arr)-1, 0

    while left <= right:
        index = (right + left)//2
        value = arr[index]
        if value > num: right = index-1
        if value < num: left = index+1
        if value == num: return index
    return -1


arr = [-8, 0, 1, 2, 4]
print binary_search(arr, 0)
