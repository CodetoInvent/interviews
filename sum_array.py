# write a method that takes in 2 int arrays of any size and returns an
# array that calculates the sum of both.

# for example, [1,2,3] and [2,3,4] will return [3,5,7]

# Or [1,2,3] and [2,3,5,5] will return [2,4,7,8]

# however, if it's like [9,9,2] and [0,1,3] you need to carry the sum so
# it returns as [1,0,0,5]

# *single digit only*


choose = lambda x, y: (x, y) if len(x) >= len(y) else (y, x)


def add(a, b, carry):
    add = a + b + carry
    carry = add / 10
    add = add % 10
    return add, carry


def sum_array(a, b):
    big, small = choose(a, b)

    carry = 0
    result = []

    i, j = len(big) - 1, len(small) - 1
    while i >= 0:
        small_value = 0 if j < 0 else small[j]
        digit, carry = add(big[i], small_value, carry)
        result.append(digit)
        i, j = i - 1, j - 1

    if carry:
        result.append(carry)

    return result[::-1]

a, b = [9, 9, 2], [9, 1, 3, 2]

print sum_array(a, b)


# def choose_array(a, b):
#     if len(a) > len(b):
#         return a, b
#     else:
#         return b, a


# def max_array(a, b):

#     big, small = choose_array(a, b)
#     delta = len(big) - len(small)
#     calculate(big, small, len(big) - 1, len(small) - 1, 0)
#     return big


# def calculate(big, small, i, j, carry):
#     if j < 0:
#         if i < 0:
#             if carry:
#                 big.insert(0, carry)
#                 return
#         else:
#             value = big[i] + carry
#             carry = add(big, i, value)
#             if carry: calculate(big, small, i - 1, j - 1, carry)
#             return

#     value = big[i] + small[j] + carry
#     carry = add(big, i, value)
#     calculate(big, small, i - 1, j - 1, carry)


# def add(big, i, value):
#     carry = value / 10
#     value = value % 10
#     big[i] = value
#     return carry


# print max_array([9, 9, 2], [9, 1, 3, 2])

# carry = 0
# for i in range(len(small))[::-1]:
#     value = small[i] + big[i + delta] + carry
#     carry = value / 10
#     value = value % 10
#     big[i + delta] = value

# if carry: big.insert(0, carry + )

# print big


# def max_array(a, b):
#     big, small = choose_array(a, b)
#     delta = (len(big) - len(small))
#     carry = 0
#     for i in range(len(small))[::-1]:
#         print small[i], big[i+ delta]
#         value = big[i+ delta] + small[i] + carry
#         carry = value / 10
#         big[i+ delta] = value % 10

#     if carry: big.insert(0, carry)
#     return big

# print max_array([9,9,2], [0,1,3, 2])
