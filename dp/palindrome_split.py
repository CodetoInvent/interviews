# how many splits does it take to turn a string into palindromes?


# the axis describe the index of the string
# 'abacc' -> 'aba', 'cc'

# _ 0 1 2 3 4
# 0 0 1
# 1   0 1
# 2     0 1
# 3       0 0
# 4         0

# - iterate through word with word size L=1..len(word)
# - check if word a palindrome
#   - if not then check if partition of it is by running through all possible splits
#   - if is then set 0 in matrix for given index


def is_palindrome(str):
  for i in range(len(str)//2):
    if str[-i-1] != str[i]: return False
  return True


def palindrome_split(str):

  result = [([0] * (len(str))) for i in range(len(str))]

  word_length, index = 1, 0
  while word_length <= len(str):

    if is_palindrome(str[index:word_length]):
      result[index][word_length-1] = 0
    else:
      # if the substring is not a palindrome then
      # iterate through all splits to find min split
      # abac -> [(a, bac), (ab, ac), (aba, c)]
      result[index][word_length-1] = min(
        [
          result[index][i] + result[i][word_length-1] + 1
          for i in range(1, word_length)
        ]
      )
    index += 1

    if index == len(str):
      word_length, index = word_length+1, 0

  return result




# tests
assert is_palindrome('abba')
assert is_palindrome('abcba')
assert is_palindrome('a')
assert not is_palindrome('abc')
assert not is_palindrome('ac')

matrix =  palindrome_split('abcbm')
for row in matrix:
  print ' '.join(map(str,row))