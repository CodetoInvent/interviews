def flip(arr, k):
  flipped = arr[:k][::-1]
  return flipped + arr[k:]

def find_max(arr, k):
  maximum, index = arr[0], 0
  for i in range(k):
    if arr[i] > maximum:
      maximum, index = arr[i], i
  return index



def pancake_sort(arr):

  for i in range(len(arr), -1, -1):
    current_max = find_max(arr, i)
    arr = flip(arr, current_max+1)
    arr = flip(arr, i)
    print arr

  return arr



if __name__ == '__main__':
  arr = [1, 5, 4, 3, 2]

  assert flip(arr, 3) == [4, 5, 1, 3, 2]

  print pancake_sort(arr)


# example

# [1, 5, 4, 3, 2]
# [5, 1, 4, 3, 2]
# [2, 3, 4, 1, 5]
# [4, 3, 2, 1, 5]
# [1, 2, 3, 4, 5]


