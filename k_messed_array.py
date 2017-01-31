import heapq


def sort(arr, k):

  heap = []

  for i in range(k): heapq.heappush(heap, arr[i])

  for i in range(len(arr)):
    if i + k < len(arr): heapq.heappush(heap, arr[i + k])
    arr[i] = heapq.heappop(heap)
 
  return arr


messed = [0, 1, 3, 2, 6, 5, 10]
print sort(messed, 2)
