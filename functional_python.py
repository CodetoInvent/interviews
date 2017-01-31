

upper_case = lambda string: string.upper()
has_space = lambda string: ' ' not in string

up = map(upper_case, ['hallo', 'test', 'was geht'])
no_space = filter(has_space, up)
concat = reduce(lambda x, y: x+y, no_space)

print concat
