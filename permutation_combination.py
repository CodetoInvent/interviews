# You are giving a list of prime numbers and you want to find all their divisors and all their combinations (in multiiplication) so for example:


def combination(nums):
    result = []

    def calc(pre, string):
        if pre: result.append(pre)
        for i in range(len(string)):
            calc(pre * string[i], string[i+1:])

    calc(1, nums)
    return sorted(result)

# print combination([2, 3, 5, 7])

def combination2(nums):
    result = []

    def calc(pre, string):
        if pre: result.append(str(pre))
        for i in range(len(string)):
            calc(str(pre) + str(string[i]), string[i+1:])

    calc(1, nums)
    return sorted(result)

# print combination2([1, 2, 3])


def max_subset(nums, n):
    result = []

    def calc(pre, string, sum):
        for i in range(len(string)):
            term = pre + '+' + string[i] if pre else string[i]
            if sum + int(string[i]) == n:
                result.append(term)
                continue
            else: calc(term, string[i+1:], sum + int(string[i]))

    calc('', nums, 0)
    return sorted(result)

# print max_subset(map(str, [2, 3, 7, 8, 4, 2]), 11)


def permutation(prefix, string):
    if not string: print prefix
    else:
        for i in range(len(string)):
            str = string[:i] + string[i+1:]
            permutation(prefix + string[i], str)

# permutation("", "ABCS")


def n_permutation(prefix, string, n):
    if n == 2: print prefix
    else:
        for i in range(len(string)):
            str = string[:i] + string[i+1:]
            n_permutation(prefix  + string[i] , str, n+1)

# n_permutation("", map(str, list(range(9))), 0)



def n_combination(nums):
    result = []

    def calc(pre, string, index):
        if index == 3: print pre
        for i in range(len(string)):
            calc(pre + string[i], string[i+1:], index+1)

    calc('', nums, 0)
    return sorted(result)

# print n_combination(map(str, range(9)))

