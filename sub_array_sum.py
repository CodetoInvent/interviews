# Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to the multiple of k, that is, sums up to n*k where n is also an integer.


# Input: [23, 2, 4, 6, 7],  k=6
# Output: True

def sub_array_sum(array, target):

	if not array or len(array) < 2: return False

	i, j = 0 = 1

	while i < len(array) and j < len(array):
		




