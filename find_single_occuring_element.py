# Find the only element in an array that only occurs once.
# Every other number occurs twice.


def find(numbers):
    bitmask = 0

    for i in numbers:
        bitmask = bitmask ^ i

    return bitmask


numbers = [1, 1, 2, 3, 3, 4, 4, 9, 9, 100, 100, 12, 12, 5, 5]
print find(numbers)

