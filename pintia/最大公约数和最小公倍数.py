M, N = input().split()
m = int(M)
n = int(N)

# 辗转相除法
# while m % n != 0:
#     m, n = n, m % n

# 更相减损术
# while m != n:
#     if m > n:
#         m = m - n
#     else:
#         n = n - m

# 穷举
gcd = 1
for i in range( min(n//2, m//2), 1, -1):
    if n % i == 0 and m % i == 0:
        n = i
        break

print(n, int(M) * int(N) // n)

