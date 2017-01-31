
a = [1, 2, 2, 3, 4, 5]
b = [2, 2, 3, 4, 5, 6, 7]


i, j = 0, 0
result = []
while i < len(a) and j < len(b):
    if a[i] > b[j]:
        j += 1
    if a[i] < b[j]:
        i += 1
    if a[i] == b[j]:
        result.append(a[i])
        i, j = i+1, j+1

print result