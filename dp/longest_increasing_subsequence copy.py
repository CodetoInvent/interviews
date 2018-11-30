
def max_subsequence_result(arr):
  i, j = 0, 1
  result = [1] * len(array)

  while j < len(array):
    if array[i] < array[j]:
      result[j] = max(
        result[j],
        result[i] + 1
      )

    i+= 1
    if i == j: i, j = 0, j+1


  return result


def backtrack_longest_subsequence(result):
  index, count = max(enumerate(subsequences), key=lambda x: x[1])

  result = []
  while count >= 1:
    if not result or arr[index] < result[-1]:
      result.append(arr[index])
      count, index = count-1, index-1
    else:
      index -= 1

  return result[::-1]


arr = [1, 2, 9, 3, 4, 5]
subsequences = max_subsequence_result(arr)
longest_subsequence = backtrack_longest_subsequence(subsequences)
print longest_subsequence
