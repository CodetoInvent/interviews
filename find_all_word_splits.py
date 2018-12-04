# given a dictionary and a word, find all word splits:
# 'hellobed' = ['hello', 'bed']

dictionary = ['hello', 'bed']

def find_words(dictionary, result, word, i):
  if i >= len(word)-1: return result

  maximum = result
  for k in range(i, len(word)):
    w = word[i:k+1]
    if w in dictionary:
      result.append(w)
      maximum = max(
        find_words(dictionary, list(result), 'hellobed', k+1),
        maximum,
        key=len
      )

  maximum = max(result, maximum, key=len)
  return maximum

print find_words(dictionary, [], 'hellobed', 0)