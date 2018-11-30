
string = 'wababbas'


def longest_palindromic_substring(string):

	if not string: return 0

	# single letter words are always palindromes
	result = [
		[
			1 if i == j
			else -1
			for j in range(len(string))
		] 
		for i in range(len(string))
	]

	# initialize 2 letter palindromes (i == i+1)
	for i in range(len(string)-1):
		k, l = string[i], string[i+1]

		if k == l: 
			result[i][i+1] = 2

	for k in range(2, len(string)):
		for j in range(len(string)-k):
			if string[j] == string[j + k] and result[j+1][j+k-1] > 0: 
				result[j][j+k] = max(
					result[j+1][j+k-1] +2,
					result[j][j+k] 
				)


	return result

	


result = longest_palindromic_substring(string)


for i in range(len(result[0])):
	for j in range(len(result)):
		if result[i][j] > 0:
			print string[i:j+1]