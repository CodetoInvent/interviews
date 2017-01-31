
n = 6
w = ' '
s = '#'
whitespace = n-1
stairs = 1
for i in range(n):
    result = w * whitespace + s * stairs
    print result
    whitespace, stairs = whitespace-1, stairs+1