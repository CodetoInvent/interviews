# Given 2 strings. Output the number of characters need to be removed from first string to make them anagrams.

from collections import defaultdict

str1 = 'abcd'
str2 = 'a'

counter = defaultdict(int)

for i in str1:
  counter[i] += 1

for i in str2:
  counter[i] -= 1

print sum([abs(i) for i in counter.values()])