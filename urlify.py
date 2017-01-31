# URLify: Write a method to replace all spaces in a string with '%20

def urlify(string):
  string = list(string)
  replacing = False
  i = 0
  while i < len(string):
    if string[i] == ' ' and replacing:
      del string[i]
      continue
    if string[i] == ' ':
      string[i] = '%20'
      replacing = True
    else:
      replacing = False
    i += 1
  return ''.join(string)
print urlify('hello         m')