

def fib(n):
  cache = [0] * (n + 1)
  def calc(n):
    if n <= 0: return 0
    if n == 1: return 1
    if cache[n] > 0: return cache[n]

    cache[n] = calc(n - 1) + calc(n - 2)
    return cache[n]
  return calc(n)

print fib(12)


def fib2(n):
  a, b = 0, 1
  for i in range(n):
    # tmp = b
    # b = a + b
    # a = tmp
    a, b = b, a + b

  return a 

print fib2(12)


def fib3(n):
  fib = [0, 1]

  for i in range(n):
    fib.append(fib[-2] + fib[-1])

  return fib[n]

print fib3(12)
