# -*- coding: utf-8 -*-

# 448. Find All Numbers Disappeared in an Array
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

# Find all the elements of [1, n] inclusive that do not appear in this array.

# Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

# Input:
# [4,3,2,7,8,2,3,1]

# Output:
# [5,6]

def find_numbers(array):
    for i in array:
        index = abs(i)-1
        if array[index] < 0: continue
        array[index] *= -1

    result = []
    for i, v in enumerate(array):
        if v > 0: result.append(i+1)

    return result


print find_numbers([4,3,2,7,8,2,3,1])
