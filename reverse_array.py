
arr = [1, 4, 3, 2]
def reverse(array):
    for i in range(len(array)//2):
        array[i], array[-i-1] = array[-i-1], array[i]
    return array

print reverse(arr)


word = 'hello'
def reverse_recursive(word):
    def helper(array, index):
        if index == len(array)//2: return array
        array[index], array[-index-1] = array[-index-1], array[index]
        return helper(array, index+1)
    reverse = helper(list(word), 0)
    return ''.join(reverse)

print reverse_recursive(word)
