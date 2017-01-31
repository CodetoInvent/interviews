

def array_left_rotation(a, n, k):
    right = a[k:]
    left = a[:k]
    return right + left
  

n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))

