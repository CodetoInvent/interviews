

def binary(n):
    digits = []
    while n:
        digit = n % 2
        n //= 2
        digits.append(digit)
    return digits[::-1]

# def convert(string, i):
#     b = binary(i)
#     string = list(string)

#     toggle = lambda c, t: c.upper() if t else c.lower()
#     choose = lambda x, y: x if len(x) <= len(y) else y
#     for i in range(1, len(choose(string, b)) + 1):
#         string[-i] = toggle(string[-i], b[-i])

#     return ''.join(string)

def convert(string, i):
    b = binary(i)
    string = list(string)

    toggle = lambda c, t: c.upper() if t else c.lower()
    i, j = len(string)-1, len(b)-1

    while j >= 0 and i >= 0:
        string[i] = toggle(string[i], b[j])
        i, j = i - 1, j - 1

    return ''.join(string)


def convert_fly(string, mask):
    string = list(string)
    for i in range(len(string)):
        capsed = mask & (1 << i)
        char = ord(string[-i-1])
        
        if capsed: char &= ~(1 << 5)
        else: char |= (1 << 5)
         
        string[-i-1] = unichr(char)
        
        # if capsed: string[-i-1] = string[-i-1].upper()
        # else: string[-i-1].lower()

    return ''.join(string)

print convert_fly("catsdogs", 8)