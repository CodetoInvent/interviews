# 9, 12, 17, 2, 4, 5 // log n

# [ 9, 12, 17 ] [ 2, 4, 5 ]


def find_pivot(arr):
   upper, lower = len(arr)-1, 0
   
   while lower <= upper:
      mid = (upper + lower)//2
      value = arr[mid]

      if value -1 < 0 or value +1 == len(arr): return -1
      right = arr[mid+1]
      left = arr[mid-1]
      
      if value > right: # value = 17
         if value > left: # 17 > 12
            return mid
         else:
            upper = mid-1
      elif value < right:
         lower = mid+1
      
   return -1


def binary_search(arr, n):
   upper, lower = len(arr)-1, 0
   
   while lower <= upper:
      mid = (upper + lower)//2
      value = arr[mid]
      if value > n:
         upper = mid-1
      elif value < n:
         lower = mid+1
      else:
         if value == n: return mid
         else: return -1
   return mid
   

def merge_array(arr, pivot):
   right, left = arr[:pivot+1], arr[pivot+1:]   
   return left + right
   
   
def main(arr, n):
   pivot = find_pivot(arr)
   if pivot == -1: return binary_search(arr, n)
   merge = merge_array(arr, pivot)
   return binary_search(merge, n)
   

      
print main([9, 12, 17, 2, 4, 5], 2)
