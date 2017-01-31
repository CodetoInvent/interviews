

arr = [1, 2, 3, 4]
total_product = reduce(lambda x, y: x * y, arr)
total_sum = sum([total_product / i for i in arr])
# print total_sum


yo = [{'y':1}, {'y':2}]
print reduce(lambda x, y: x['y'] + y['y'], yo)