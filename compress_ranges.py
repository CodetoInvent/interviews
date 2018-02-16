# given an array output ranges
# [1,2,3,4,5] => [1-5]
# [1,3,4,5,7] => [1-1,3-5,7-7]


def ranges(arr):
  i, j = 0, 1

  result = []
  while i < len(arr) and j < len(arr):
    if arr[j-1] == arr[j]-1:
      j += 1
    else:
      result.append((arr[i], arr[j-1]))
      i, j = j, j+1

  result.append((arr[i], arr[j-1]))
  return result

print ranges([1, 3, 4, 5])

