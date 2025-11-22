import math


def is_prim(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


n = int(input())
for p in range(2, n):
    if is_prim(p) and is_prim(n - p):
        print(f'{n} = {p} + {n - p}')
        break
