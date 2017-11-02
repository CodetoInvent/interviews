import heapq

def in_sort(arr):

    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j=j-1

    return arr


def heap_sort(arr, k):
    heap = arr[:k]
    heapq.heapify(heap)

    for i in range(k+1, len(arr)-1):
        arr[i-(k+1)] = heapq.heappop(heap)
        heapq.heappush(heap, arr[i])
    for i in range(k):
        arr[len(arr)-k-1 + i] = heapq.heappop(heap)
    return arr


print heap_sort([1, 2, 3, 0], 2)



def insertionsort(arr):

    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return arr

print insertionsort([1, 2, 3, 0])