# find the increasing subsequence that has the maximum sum


# arr          [4, 6,  1, 3,  8, 4,  6]
# tracking sum [4, 10, 1, 4, 18, 8, 10]


def max_sum_subsequence(arr):
  result = arr[::]

  for j in range(1, len(arr)):
      result[j] = max(
        [
          result[i] + arr[j]
          for i in range(j)
          if arr[i] < arr[j]
        ] + [result[j]]
      )
  return result


print max_sum_subsequence([4, 6, 1, 3, 8, 4, 6])
