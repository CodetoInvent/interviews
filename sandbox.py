

# def product(index, arr):
#     i = 0
#     p = 1
#     while i < len(arr) -1:
#         index = index if index < len(arr) else 0
#         p *= arr[index]
#         i += 1
#     return p


# # [1 2 3]
# def total_sum(arr):
#     if not arr: return 0
#     sum = 0
#     for i, v in enumerate(arr):
#         sum += product(i+1, arr)

#     return sum
# print total_sum([1, 2, 3])
# # arr = [1, 2, 3]
# # s = reduce(lambda x, y: x*y, arr)
# # print sum([s//i for i in arr])

# import string
# def rot_alpha(n):
#     from string import ascii_lowercase as lc, ascii_uppercase as uc
#     lookup = string.maketrans(lc + uc, lc[n:] + lc[:n] + uc[n:] + uc[:n])
#     return lambda s: s.translate(lookup)

# print rot_alpha(13)('Hello,! World') # Uryyb Jbeyq

# print[unichr(i) for i in range(ord('a'), ord('z') + 1)]


# permutations - fb interview example
# https://gist.github.com/alexrios/98e90da69ce65b48b7d2

data = ['a,123', 'b,456', 'c,789']

print reduce(lambda x, y: x + y.split(',')[-1], data)

r = reduce(lambda x, y: x +';' +y.split(';')[-1], r[1])