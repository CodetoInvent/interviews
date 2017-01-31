# Find n in a rotated array

# Input:
# [5, 6, 7, 8, 1, 2, 3, 4], n = 2


def find_pivot(array):
    left, right = 0, len(array) - 1

    while left <= right:
        index = (left + right) // 2

        if index < len(array)-1 and array[index] > array[index +1]:
            return index

        if array[index] >=  array[left]: left = index + 1
        else: right = index - 1
    return left


def partial_binary_search(numbers, pivot, n):
    left, right = (0, pivot)
    if numbers[-1] >= n: left, right = pivot, len(numbers)-1

    while left <= right:
        index = (left + right) // 2
        value = numbers[index]

        if value > n: right = index - 1
        if value < n: left = index + 1

        if value == n: return index, n

    return -1, -1





n = 2
numbers = [3, 4, 1, 2]
pivot = find_pivot(numbers)
print pivot
index, number = partial_binary_search(numbers, pivot, n)

print index, number