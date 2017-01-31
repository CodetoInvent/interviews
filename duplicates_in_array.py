# -*- coding: utf-8 -*-

# 442. Find All Duplicates in an Array
# https://leetcode.com/problems/find-all-duplicates-in-an-array/

# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

# Find all the elements that appear twice in this array.

# Could you do it without extra space and in O(n) runtime?

# Input:
# [4,3,2,7,8,2,3,1]

# Output:
# [2,3]


# t: O(n) s: O(1)
def find_duplicates(array):

    result = []
    for i in array:
        index = abs(i)-1
        if array[index] < 0: result.append(abs(i))
        array[index] *= -1

    return result


# t: O(n) s: O(n)
def find_duplicates_hash(array):
    hashset = set()

    result = []
    for i in array:
        if i in hashset: result.append(i)
        else: hashset.add(i)
    return result


assert find_duplicates([4, 3, 2, 7, 8, 2, 3, 1]) == [2, 3]
assert find_duplicates_hash([4, 3, 2, 7, 8, 2, 3, 1]) == [2, 3]