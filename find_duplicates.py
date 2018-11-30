# input:  arr1 = [1, 2, 3, 5, 6, 7], arr2 = [3, 6, 7, 8, 20]

def find_duplicates(arr1, arr2):

	if not arr1 or not arr2: return []

	longer, shorter = (arr1, arr2) if len(arr1) > len(arr2) else (arr2, arr1)

	duplicates = []
	for i in shorter:
		if binary_search(longer, i):
			duplicates.append(i)

	return duplicates


def binary_search(arr, number):

	if not arr: return False

	left, right = 0, len(arr) -1

	while left <= right:
		mid = (left + right) / 2

		if arr[mid] > number: 
			right = mid - 1
		if arr[mid] < number:
			left = mid + 1
		if arr[mid] == number:
			return True

	return False



assert find_duplicates([1, 2, 3, 5, 6, 7], [3, 6, 7, 8, 20]) == [3, 6, 7]
assert find_duplicates([1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12], [3, 6, 7, 8, 20]) == [3, 6, 7, 8]
assert find_duplicates([], [3, 6, 7, 8, 20]) == []
assert find_duplicates([3, 6, 7, 8, 20], []) == []
assert find_duplicates([1, 2], [1, 2]) == [1, 2]

assert binary_search([1, 2, 3, 5, 6, 7], 7) == True
assert binary_search([1, 2, 3, 5, 6, 8], 7) == False
assert binary_search([], 7) == False
