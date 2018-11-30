

def shifted_array_search(arr, number):

	if not arr: return -1

	pivot = find_pivot(arr)


def find_pivot(arr):

	if not arr: return -1

	left, right = 0, len(arr) - 1

	while left <= right:
		mid = (left + right) / 2
		
		i, j = arr[mid], arr[mid + 1]

		if i < j:
			left = mid + 1
		if i > j:
			return mid