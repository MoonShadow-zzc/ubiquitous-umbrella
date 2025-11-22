n = int(input())
for i in range(n):
    a, b, c, = map(int, input().split())
    if a ** 2 + b ** 2 + c ** 2 == 3 * a * b * c:
        print('Yes')
    else:
        print('No')
