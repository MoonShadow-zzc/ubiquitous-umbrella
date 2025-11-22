import math


def prime(p):
    if p == 1:
        return False
    if p == 2:
        return True
    for i in range(2, math.ceil(math.sqrt(p))+1):
        if p % i == 0:
            return False
    return True


def prime_sum(m, n):
    primes = []
    for i in range(m, n + 1):
        if prime(i):
            primes.append(i)
    # print(primes)
    return sum(primes)


m, n = input().split()
m = int(m)
n = int(n)
print(prime_sum(m, n))
