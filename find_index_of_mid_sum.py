
# find index in array where the left side and the right side have the same sum


def find_index(arr):

  left, right = 0, sum(arr)
  for i in range(1, len(arr)):
    left, right = left + arr[i-1], right - arr[i-1]
    print left, right

    if left == right:
      return i

  return -1

print find_index([1, 2, 6, 0, 1, 7, 1])