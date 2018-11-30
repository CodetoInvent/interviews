# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
  def reverseKGroup(self, head, k):
    length = get_length(head)

    groups = length % k

    for i in range(groups):
      


  def get_len(self, head):

    length = 0
    node = head

    while node:
      length += 1
      node = node.next

    return length