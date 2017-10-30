# [1, 100], [1, 2, 12, 20, 50, 100] -> [[2, 11], [13, 19], [21, 49], [51, 99]]

# remove cases:
# [1, 100] -> 1   : [[2, 100]]
# [1, 100] -> 100 : [[1, 99]]
# [1, 100] -> 50  : [[1, 49], [51, 100]]

def remove_ranges(ranges, remove):
  # sort remove indices it runs in O(n)
  remove = sorted(remove)
  result = [ranges]

  i = j = 0
  while j < len(remove):
    if result[i][1] < remove[j]:
      i+= 1
      continue

    current_range = result.pop(i)

    if remove[j] == current_range[0]:
      new_range = [[current_range[0]+1, current_range[1]]]
    elif remove[j] == current_range[1]:
      new_range = [[current_range[0], current_range[1]-1]]
    else:
      new_range = [
        [current_range[0], remove[j]-1],
        [remove[j]+1, current_range[1]]
      ]


    if new_range[0][0] <= new_range[0][1]:
      result[:i] += new_range

    j+=1

  return result

print remove_ranges([1, 100], [1, 2, 3, 4, 50, 51, 96, 100])
