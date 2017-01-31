import math 

# only works for positive integers for now
def multiply(x, y):
    if x == 0 or y == 0: return 0

    remainder = y % 2
    shift = int(math.log(math.fabs(y) - remainder, 2))

    result = (x << shift) + (remainder * x)
    return result


def multiply2(x, y):
    if x == 0 or y == 0: return 0

    result = 0
    for _ in range(int(math.fabs(y))):
        result += x

    return result if (y > 0) else ~result+1

print multiply(2, 16)
print multiply2(-2, 16)