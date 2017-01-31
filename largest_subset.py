# Largest Subset With Consecutive Numbers


def subset(arr):
    hashset = set(arr)
    subsets = []
    for i in arr:
        if i-1 in hashset: continue

        j = i
        sequence = []
        while j in hashset:
            sequence.append(j)
            j += 1

        subsets.append(sequence)

    return subsets


arr = [1, 3, 16, 11, 4, 7, 5, 6, 10, 12, 14]
arr = subset(arr)
print arr
