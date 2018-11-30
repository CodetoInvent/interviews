
dictionary = {
  'Key1': '1',
  'Key2': {
    'a' : '2',
    'b' : '3',
    'c' : {
      'd' : '3',
      'e' : '1'
      }
    }
}




  def flatten(dictionary, key, result):
    for k, v in dictionary.items():
      new_key = '.'.join([key, k]) if key else k
      if type(v) == str: result[new_key] = v
      else:
        flatten(v, new_key, result)
    return result


  print flatten(dictionary, '', {})


  def flatten(dictionary):
    queue = []
    for k, v in dictionary.items(): queue.append((k, v))

    result = {}
    while queue:
      key, value = queue.pop()

      if type(value) == str:
        result[key] = value
        continue
      
      for k, v in value.items():
        new_key = '.'.join([key, k])
        queue.append((new_key, v))

    return result

  print flatten(dictionary)
