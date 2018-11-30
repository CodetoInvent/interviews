


def generate_parens(n):
	return helper(n, 0, 0, '', [])


def helper(n, opened, closed, str, parens):
	
	if opened == n and closed == n: 
		parens.append(str)

	if opened < n:
		helper(n, opened + 1, closed, str + '(', parens)

	if closed < n:
		if closed < opened:
			helper(n, opened, closed + 1, str + ')', parens)


	return parens


print generate_parens(3)