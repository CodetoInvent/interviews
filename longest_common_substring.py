

#   _ a b c d e
# _ 0 0 0 0 0 0
# a 0 1 1 1 1 1
# d 0 1 1 1 2 2
# c 0 1 1 2 2 2
# e 0 1 1 2 2 3

# algorithm:
#
# if characters are the same:
#   result[i][j] = result[i-1][j-1]+1
# else:
#   result[i][j] = 0


def longest_common_substring(str1, str2):

  result = [[0] * (len(str2) + 1) for i in range(len(str1) + 1)]

  for row in range(1, len(str1)+1):
    for column in range(1, len(str2)+1):
      result[row][column] = \
        result[row-1][column-1] + 1 \
        if str1[row-1] == str2[column-1] \
        else 0

  return result

print longest_common_substring('abcd', 'abc')