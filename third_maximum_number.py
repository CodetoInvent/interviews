# 414. Third Maximum Number
# https://leetcode.com/problems/third-maximum-number/

# Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

# Input: [3, 2, 1]
# Output: 1

# Java: t: O(n) s: O(n)
# int thirdMaxiumum(int[] numbers){
#   PriorityQueue<Integer> heap = new PriorityQueue<Integer>((a, b) -> b - a);

#   for (int num : numbers){
#     heap.offer(num);
#   }

#   int maximum = numbers[0];
  
#   for (int i = 0; i < 3; i++){
#     if (!heap.isEmpty()) maximum = heap.poll();
#     else break;
#   }
#   return maximum;
# }


# Python: t: O(n) s: O(n)

import heapq

def third_largest_number(numbers):
  heap = []

  for i in numbers: heapq.heappush(heap, (-i, i))

  maximum = None
  for _ in range(3):
    if heap: 
      maximum = heapq.heappop(heap)[1]
    else: break

  return maximum

print third_largest_number([2, 3, -10, 1])

