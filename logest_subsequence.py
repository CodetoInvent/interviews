



def subsequence(str1, str2):
  maximum = 0
  matrix = [[0 for i in range(len(str2)+1)] for i in range(len(str1)+1)]

  for i in range(1, len(matrix)):
    for j in range(1, len(matrix[i])):
      if str1[i-1] == str2[j-1]: 
        matrix[i][j] = matrix[i-1][j-1]+1
      else:
        matrix[i][j] = max(matrix[i][j-1], matrix[i-1][j])

      if matrix[i][j] > maximum: maximum = matrix[i][j]

  return maximum


str1 = "ABCDGHLQR";
str2 = "AEDPHR";
print subsequence(str1, str2)