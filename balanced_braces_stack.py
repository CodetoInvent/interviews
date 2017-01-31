
# You are given a sequence of braces and have to determine whether they
# make sense mathematically.

check = {
    '()()()': True,
    '(()())': True,
    ')()(': False,
    '({[][]})': True,
    '{[}]': False
}

start_brace = '('
end_brace = ')'

braces = {'}': '{', ']': '[', ')': '('}

def validate_braces(str):
    stack = []
    for i in str:
        if i not in braces: 
            stack.append(i)
            continue
        
        if not stack: return False
        pop = stack.pop()
        if braces[i] != pop: return False
    return True


for i, v in check.items(): 
    assert validate_braces(i) == v

