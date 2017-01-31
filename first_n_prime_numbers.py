# Sieve of Eratosthenes


def primes(n):
    n+=1

    prime_numbers = []
    not_primes = [False] * n

    for i in range(2, n):

        if not_primes[i]: continue

        for j in range(i*2, n, i):
            not_primes[j] = True

        prime_numbers.append(i)

    return prime_numbers

print primes(10)