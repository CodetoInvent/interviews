import math
x = -123

result = 0
length = int(math.log10(abs(x)))+1
negative = x < 0
x = abs(x)
for i in range(length):
    digit = x % 10
    x //= 10
    result += digit * math.pow(10, i)

result = int(result)
result = -result if negative else result
print result