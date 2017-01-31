
from collections import defaultdict


def most_frequent(numbers):
    counter = defaultdict(int)

    for i in numbers: counter[i] += 1

    maximum = (-1, -1)

    for i, v in counter.items():
        if v > maximum[1]:
            maximum = (i, v)

    return maximum



numbers = [1, 1, 1, 2, 2, 3, 1, 2]
print most_frequent(numbers)