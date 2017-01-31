
def parens(left, right, string):
    if not left and not right:
        print string

    if left > right: return
    if left > 0:
        parens(left - 1, right, string + '(')
    if right > 0:
        parens(left, right - 1, string + ')')

n = 4
parens(n, n, '')


