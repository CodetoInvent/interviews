#   _ a b c d e
# _ 0 0 0 0 0 0
# a 0 1 1 1 1 1
# d 0 1 1 1 2 2
# c 0 1 1 2 2 2
# e 0 1 1 2 2 3


def longest_subsequence(str1, str2):

  str1, str2 = list(str1), list(str2)

  subsequences = [([0] * (len(str2)+1)) for i in range(len(str1)+1)]

  for row in range(1, len(str1)+1):
    for column in range(1, len(str2)+1):
      subsequences[row][column] = max(
        subsequences[row-1][column],
        subsequences[row][column-1]
      ) + (1 if str1[row-1] == str2[column-1] else 0)

  return subsequences


print longest_subsequence('abcd', 'acd')