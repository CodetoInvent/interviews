# Find the two flavours of ice cream who amount to m


def index(arr, n, m):

    def find(number):
        for i in range(len(arr)):
            if arr[i] == number:
                arr[i] = -arr[i]
                return i
        return -1

    return (find(n), find(m))


def binary_search(arr, left_pad, n):
    if not arr: return -1

    left, right = left_pad, len(arr)-1

    while left <= right:
        middle = (left + right)//2
        found = arr[middle]

        if found == n: return n
        if found > n: right = middle-1
        if found < n: left = middle+1

    return -1

def search_flavours(arr, money):
    if not arr or money <= 0: return 0

    sorted_ice_creams = sorted(arr)

    for i, v in enumerate(sorted_ice_creams):
        complement = money - v
        index = binary_search(sorted_ice_creams, i+1, complement)
        if index != -1: return v, complement

    return 0, 0

def main(arr, money):
    n, m = search_flavours(arr, money)
    i, j = index(arr, n, m)

    return i, j


ice_creams = [1, 4, 5, 3, 4]
money = 7

print main(ice_creams, money)