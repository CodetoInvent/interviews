# Find pairs in an integer array whose sum is equal to 10


def pairs(numbers):

    hashset = set(numbers)
    result = set()

    for i in numbers:
        if i >= 10: continue
        complement = 10 - i
        if complement in hashset:
            pair = min(i, complement), max(i, complement)
            if pair in result: continue
            result.add(pair)

    return result

numbers = [1, 9, 1, 2, 8]
print pairs(numbers)
