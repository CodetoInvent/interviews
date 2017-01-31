# From a list of integer intervals, write a function to minimize the number of overlapping or consecutive ones. 

# Test Input: [4, 8], [3, 5], [-1, 2], [10, 12] 
# Test ouput: [-1, 8], [10,12]
#
# Sorted: [[-1, 2], [3, 5], [4, 8], [10, 12]]


def range_overlap(ranges):
  ranges = sorted(ranges, key=lambda range: range[1])
    
  i = 0
  while i < len(ranges) - 2:
    left = ranges[i]
    right = ranges[i + 1]
    if left[1] >= right[0] -1: merge(left, right, ranges, i)
    else: i += 1

  return ranges

def merge(left, right, ranges, index):
  minimum = min(left[0], right[0])
  maximum = max(left[1], right[1])
  ranges[index] = [minimum, maximum]
  del ranges[index +1]


print range_overlap([[4, 8], [3, 5], [-1, 2], [10, 12] ])