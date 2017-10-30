# -*- coding: utf-8 -*-

# 303: https://leetcode.com/problems/range-sum-query-immutable

# Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

# Example:
# Given nums = [-2, 0, 3, -5, 2, -1]

# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3
# Note:
# You may assume that the array does not change.
# There are many calls to sumRange function.

nums = [-2, 0, 3, -5, 2, -1]

def sumRange(nums, i, j):
  if j-i > i + len(nums) - 1: return 0

  total_sum = 0
  while i <= j:
    total_sum += nums[i]
    i += 1
  return total_sum

print sumRange(nums, 0, 6)


def sumRangeDynamic(nums, total, i, j):
  if i > j: return total
  return sumRangeDynamic(nums, total + nums[i], i+1, j)

print sumRangeDynamic(nums, 0, 0, 5)