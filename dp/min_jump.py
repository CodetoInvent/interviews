# given an array of integers, how many jumps do you need to reach the end of the array? you can jump by the value indicated in the array at any given index.

# algorithm:
# - check if you can reach j from i
#   - if yes then result[j] = min(result[j], result[i]+1)
#
# [2, 3, 1, 1, 2, 4, 2, 0, 1, 1]

import sys

def min_jump(arr):

  result = [sys.maxint] * len(arr)
  result[0] = 0

  for j in range(1, len(arr)):
    result[j] = min(
      [
        result[i] + 1
        for i in range(j)
        if arr[i] + i >= j
      ] + [result[j]]
    )

  return result


print min_jump([2, 3, 1, 1, 2, 4, 2, 0, 1, 1])
