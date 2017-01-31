arr = [-2,1,-3,4,-1,2,1,-5,4]


maximum = arr[0]
current = arr[0]

for i in arr[1:]:
    current += i
    if current < 0: current = 0
    if current > maximum: maximum = current

    # current = max(0, current + i)
    # maximum = max(current, maximum)

print maximum

