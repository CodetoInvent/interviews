# 53. Maximum Subarray: https://leetcode.com/problems/maximum-subarray

# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.

def kadane(arr):

  maximum = arr[0]
  current = arr[0]

  for i in arr[1:]:
      current = max(0, current + i)
      maximum = max(current, maximum)

      # current += i
      # if current < 0: current = 0
      # if current > maximum: maximum = current

  return maximum

print kadane([-2,1,-3,4,-1,2,1,-5,4])


def dynamic(arr):
  result = [0] + arr

  for i in range(1, len(arr)):
    result[i] = max(
      result[i-1] + arr[i-1],
      result[i]
    )

  return max(result)

print dynamic([-2,1,-3,4,-1,2,1,-5,4])

