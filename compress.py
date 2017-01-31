
word = 'aaaaaabccccd'
compressed = 'a6b1c4d1'

def compress(word):
  word, result = list(word), []
  last, word_count = word[0], 1
  i = 1

  while i <= len(word):
    char = word[i] if i < len(word) else None

    if char == last:
      word_count += 1
    else:
      result.append(last + str(word_count))
      word_count = 1
      last = char
    i += 1

  return ''.join(result)

print compress(word)