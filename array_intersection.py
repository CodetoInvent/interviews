from collections import defaultdict

a = [2, 3, 4, 4, 6, 7, 8, 9]
b = [1, 99, 4, 6, 7, 8, 9, 2]

counter = defaultdict(int)
for i in a:
    counter[i] += 1

result = []
for i in b:
    if i in counter and counter[i]:
        result.append(i)
        counter[i] -= 1

print result
