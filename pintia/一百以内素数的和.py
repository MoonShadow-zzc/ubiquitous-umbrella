def prime(p):
    if p == 1:
        return False
    for i in range(2, p):
        if p % i == 0:
            return False
    return True


primes = []
for i in range(1, 51):
    if prime(i):
        primes.append(i)
print('50以内的素数有：', primes)
print('其和为：', sum(primes))
