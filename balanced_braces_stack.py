
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

        if not stack or braces[i] != stack.pop():
            return False
    return True


for i, v in check.items():
    assert validate_braces(i) == v

def validate_braces(string):
    balance = 0

    for i in string:
        if i == '(':
            balance += 1
        if i == ')':
            balance -= 1
        if balance < 0:
            return False

    return balance == 0