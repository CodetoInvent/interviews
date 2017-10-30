
def min_edit_distance(str1, str2):
  str1, str2 = list(str1), list(str2)

  distances = [([0] * (len(str2)+1)) for i in range(len(str1)+1)]

  # init initial rows for 0th row & 0th column for difference to empty string
  for i in range(len(str1)): distances[i][0] = i
  for i in range(len(str2)): distances[0][i] = i

  for row in range(1, len(str1)+1):
    for column in range(1, len(str2)+1):
      if str1[row-1] == str2[column-1]:
        distances[row][column] = distances[row-1][column-1]
      else:
        distances[row][column] = min([
          distances[row-1][column-1],
          distances[row-1][column],
          distances[row][column-1],
        ]) + 1

  return distances


str1 = 'abcd'
str2 = 'abcd'

print min_edit_distance(str1, str2)
