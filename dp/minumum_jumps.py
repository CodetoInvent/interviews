# Minimum jumps in an array to reach the end of the array
#
# [1, 4, 3, 7, 1, 2, 6, 7, 6, 10] -> 3 jumps

import heapq

def minimum_jumps(arr):
    if not arr: return 0
    heap = []

    i = 1
    ladder = arr[0]
    counter = 1
    while i < len(arr):
        if not ladder:
            ladder = abs(heapq.heappop(heap))
            counter += 1
        value = arr[i]
        heapq.heappush(heap, -value)
        i += 1
        ladder -= 1
    return counter


arr = [2, 3, 1, 1, 2, 4, 2, 0, 1, 1]

print minimum_jumps(arr)

