from collections import defaultdict

word = 'aaccbcabc'
alphabet = ['a', 'b', 'c']

min_ = lambda x, y: x if len(x) < len(y) else y

def shortest_substring(word, alphabet):
  minimum = word
  counter = defaultdict(set)
  chars = set()
  i = j = 0

  while i < len(word) and j < len(word):
    if word[j] in alphabet:
      counter[word[j]].add(j)
      chars.add(word[j])

    if len(chars) == len(alphabet):
      minimum = min_(word[i:j+1], minimum)
      last = word[i]

      if counter[last]: counter[last].remove(i)
      if not counter[last]: chars.remove(last)

      i+=1
    else:
      j+=1

  return minimum


print shortest_substring(word, alphabet)
