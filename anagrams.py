# How many characters need to be changed before I can make it an anagram?
from collections import defaultdict

a = 'cde'
b = 'edc'

# count = [0] * 26

# for i in a:
#     index = ord(i) - ord('a')
#     count[index] += 1

# for i in b:
#     index = ord(i) - ord('a')
#     count[index] -= 1

# print reduce(lambda x,y : x+y, map(abs, count))

counter = defaultdict(int)

for i in a: counter[i] += 1
for i in b: counter[i] -= 1

print sum(map(abs, counter.values()))
