# Find the two flavours of ice cream who amount to m

from collections import defaultdict

def main(arr, money):
    count = create_map(arr)
    flavours = find_flavours(arr, money, count)
    return flavours


def create_map(arr):
    count = defaultdict(list)

    for i, v in enumerate(arr):
        count[v].append(i)

    return count

def find_flavours(arr, money, count):
    for i, v in enumerate(arr):
        complement = money - v
        if complement in count:
            for j in count[complement]:
                if j != i: return (j, i)

    return (-1, -1)


ice_creams = [1, 4, 5, 3, 4]
money = 7

print main(ice_creams, money)