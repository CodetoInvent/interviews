
a = [1, 2, 3, 4, 5]
b = [2, 3, 4, 5, 7]

result = []

bigger = lambda x, y: (x, y) if len(x) >= len(y) else (y, x) 

big, small = bigger(a, b)

while small and big:
    if big[0] > small[0]:
        result.append(small.pop(0))
    else:
        result.append(big.pop(0))

print result + big

