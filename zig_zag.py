str = "AB"

def convert(str, rows):
	if rows == 1: return str
	counter, down = 0, True
	result = [[] for row in range(rows)]
	for i, s in enumerate(str):
		result[counter].append(s)
		counter = counter + 1 if down else counter - 1

		if counter == rows -1:
			down = False

		if counter == 0:
			down = True


	return result

print "".join(sum(convert(str, 1), []))