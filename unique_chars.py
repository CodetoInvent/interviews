# unique characters in string
# ctci 1.1



def check_unique(string):
    vector = 0
    
    for i in string:
        bit = ord(i) - ord('a')
        if (vector & (1 << bit)) > 0:
            return False
        vector |= (1 << bit)

    return True


print check_unique('halo')


# check permutation of palindrom
def perm(string):
    vector = 0

    for i in string:
        # making the character lower case
        val = ord(i)
        # making it lower case 
        val |= (1 << 5)
        # making it upper case
        # val &= ~(1 << 5)
        char = val - ord('a')
        mask = 1 << char

        vector ^= mask

    # return True if all characters even number, or only one odd
    return vector == 0 or (vector & (vector - 1) == 0)


print perm("Halah")


def compress(string):
    result = ""
    current = string[0]
    count = 0
    for i in string:
        if current == i:
            count += 1
        else:
            result += current + str(count)
            current = i
            count = 1

    if result[-2] != current: result += current + str(count)
    return result


print compress("aaaabbbbc")


# 1.5
def one_off(string, other):
    vector = 0
    if len(string) not in [len(other), len(other) +1, len(other) - 1]: return False

    def shift(s, vector):
        for i in s:
            val = ord(i)
            val |= (1 << 5)
            char = val - ord('a')
            mask = 1 << char
            vector ^= mask
        return vector

    vector = shift(string, vector)
    vector = shift(other, vector)

    return vector & (vector - 1) == 0

print one_off("pale", "ple")


def palindrome(s):
    for i in range(len(s)/2):
        if s[i] != s[len(s)-i-1]: return False

    return True


print palindrome('hallollah')