from collections import deque

arr = [3, 1, 9, 10, 4, 11]

def target_sum(arr):
    i = j = 1

    last_pick = arr[0]
    total_sum = arr[0]
    picks = deque([arr[0]])
    
    while i < len(arr)-1 and j < len(arr)-1:
        if arr[i] >= last_pick:
            last_pick = arr[i]

